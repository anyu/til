# Cypress

## Setup

```
npm install cypress --save
npx cypress open
```

## Misc gotchas

If two network calls are made to the same URL in quick succession without actions in between,
may need to make use of the `times` option in the RouteMatcher for Cypress to mock out the right calls:
https://github.com/cypress-io/cypress/issues/4460#issuecomment-839027753

## Example e2e test

```js
const SELECTORS = {
  someInput: 'email'
}

describe('Some flow', () => {

  it('does something', ()=> {

    cy.visit('http://localhost:3000')

    cy.getByCy(SELECTORS.someInput).type("some_email")

    // Cypress intercepts network calls in inverse order (?)
    // Also note the use of `times` within the intercept functions for these calls
    cy.intercept(SOME_EXTERNAL_URL, { times: 1 },
    {
      statusCode: 200,
      fixture: 'fixtureFile.json',
    })
    .as('mockedCall_2')

    cy.intercept(SOME_EXTERNAL_URL, { times: 1 },
    {
      statusCode: 200,
      fixture: 'fixtureFile.json',
    })
    .as('mockedCall_1')

    cy.getByCy(SELECTORS.signInForm).submit()

    // `wait` seems to expect them in chronological order
    cy.wait('@mockedCall_1')
    cy.wait('@mockedCall_2')

    cy.url().should('eq', 'http://localhost:3000/')
  })
```