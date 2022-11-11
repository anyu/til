# AWS Cognito

## What is it?

[AWS Cognito](https://docs.aws.amazon.com/cognito/index.html) is a service that provides user authentication/authorization/user management for web or mobile apps.

### Other supported features
- Authenticate users via 3rd party identity providers + provide temporary security creds to allow accessing your app's backend resources in AWS or another service behind Amazon API Gateway.
- Synchronize data across user devices. Your app can save data locally on users' devices, so the app works even when devices are offline.
- Currently allows up to 40m users per user pool

### Tradeoffs

**Pros**
- Can be cheaper than other providers
- Can integrate with common 3rd party providers
- SDKs available in various languages (but docs/support may be questionable?)

**Cons**

- apparently the workflow is inflexible
- security options are expensive per user

### "Products"
- [Cognito user pools](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-identity-pools.html)
  - user pools are user directories in Cognito, with which users can sign into your app or through a 3rd-party ID provider. All memberse of the user pool will have a directory profile accessible via the SDK.
- [Cognito identity pools](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-identity.html) (aka. federated identities)
  - identity pools provide AWS credentials to grant users access to other AWS services)

You can use the two types of pools separately or together (eg. configure an identity pool to exchange user pool tokens for AWS creds)

### User Pools

#### Configuring a user pool
1. Create a user pool
2. Create an app client (get an app client ID)
3. Choose `Cognito User Pool` as the `Enabled Identity Provider` in the app client settings.
4. Provide 
  - a callback URL for Cognito's auth server to call after users are authenticatd.
  - a sign out URL
5. Choose `Authorization code grant` to get an auth code that can be exchanged for user pool tokens. User pool tokens are never exposed to end users.
6. Choose `Implicit grant` to get user pool JWT tokens returned by Cognito. This can be used when there's no backend available to exchange an auth code for tokens (or for debugging)

After successfully authenticating a user, Amazon Cognito issues JSON web tokens (JWT) that you can use to secure and authorize access to your own APIs, or exchange for AWS credentials.

#### Granular authentication flow

1. User signs into app -> Cognito checks login info. On success, Cognito creates a session and returns an ID, access, and refresh tokens.
2. The session cookies have an expiry of 1 hour. If the user has ID tokens that expire within the hour, they can refresh their tokens without re-authenticating.

#### The ID token

The ID token is a JWT, and contains identity claims about the user that can be used in your app. It can also be used to auth users to your resources.
- the token header contains a key ID and algorithm.
- the token payload contains claims about the user (eg. name, email, etc)
- the token signature jeeds to be verified if used by external applications

#### The access token

The access token is also a JWT, and is used to authorize API operations in the context of a user in the pool.
For example, you can use it to grant the user access to add/delete/change user attributes.

- the token header contains a key ID and algorithm (the key ID is different from that of the ID token, since different keys are used to sign them)
- the token payload contains claims about the user, a list of the user's groups and scopes.
- the token signature jeeds to be verified if used by external applications

The access token expiry can be set between: 5mins to 1 day (though if using Amazon Cognito HostedUI, which has cookies valid for an hour, you can't set the expiry lower than an hour)

#### The refresh token

The refresh token is used to retrieve new ID and access token.

The refresh token expires in 30 days by default. It can be set between: 60mins to 10 years.

### If using User Pools + Identity Pools

A typical flow would involve:
1. User signs in via user pool. Receives user pool tokens.
2. App exchanges user pool tokens for AWS creds via identity pool.
3. User uses those AWS creds to access other AWS services. 

## Using the various JS libraries

Confusingly, there are 3 official JS libraries to pick from:
- [Amplify](https://docs.amplify.aws/lib/auth/getting-started/q/platform/js)
- [amazon-cognito-identity-js](https://github.com/aws-amplify/amplify-js/tree/main/packages/amazon-cognito-identity-js)
- [AWS SDK for JavaScript](https://github.com/aws/aws-sdk-js-v3) (on v3)
  - [client-cognito-identity-provider](https://github.com/aws/aws-sdk-js-v3/tree/main/clients/client-cognito-identity-provider)
  - [client-cognito-identity](https://github.com/aws/aws-sdk-js-v3/tree/main/clients/client-cognito-identity)

### Amplify

Amplify is an umbrella of a bunch of a services, one of which is Cognito.
- primarily a client lib for browser or mobile apps, but can be used on backend with SSR frameworks (eg. Next.js)
- does not support secrete-enabled Cognito apps
- can only use admin-level Cognito APIs indirectly via [Admin Actions](https://docs.amplify.aws/cli/auth/admin/)

**When to use**: whenever building a client-side app and need other tools from the Amplify ecosystem

### amazon-cognito-identity-js

Originally a standalone library that got migrated into the Amplify monorepo. Amplify actually just uses this package to make Cognito API requests.
- can be used without Amplify
- essentially a nice wrapper around lower-level AWS SDK calls (note: it does not use `aws-sdk` packages, but makes HTTP calls to AWS directly)
- works on backend
- when used on frontend, provides lower level Cognito API calls
- does not support secret-enabled Cognito apps
- cannot use admin-level Cognito APIs (those that require AWS credentials)

**When to use**: whenever you don't need the other Amplify features. Can be used in backend but limited to public Cognito APIs.

#### Usage Notes
- seems like the `getSession` call handles refreshing auth tokens with a non-expired refresh token on your behalf transparently, so this should not have to be manually done

#### Code Examples
- https://mpace.medium.com/working-with-cognito-authn-f479b7d2b5b6

### AWS SDK for JavaScript

This is the 'lowest level' option. Exposes all the operations you can run in AWS.
- works on backend
- on frontend, may be better off using Amplify or amazon-cognito-identity-js since they provide nice wrappers
- supports secret-enabled Cognito clients
- can use admin-level Cognito APIs

**When to use**: whenever you need to access protected Cognito APIs that require dev creds.

#### Usage Notes

Confusingly, there are two very closely named packages.

For just user pools, we should only need [client-cognito-identity-provider](https://github.com/aws/aws-sdk-js-v3/tree/main/clients/client-cognito-identity-provider).

[client-cognito-identity](https://github.com/aws/aws-sdk-js-v3/tree/main/clients/client-cognito-identity) seems to be for if you also need to use identity pools.

**Refreshing auth tokens**
- I *think* this needs to be taken care of manually...
  - via the [InitiateAuth](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_InitiateAuth.html) API call

#### Code Examples
- https://github.com/Mifrill/bug-reproduce-aws-sdk-js-v3-missing-refresh-token/
- https://github.com/maximivanov/cognito-js-usage (basic usage, also differentiates between browser and server)

---

## Resources
- [AWS: What is Amazon Cognito](https://docs.aws.amazon.com/cognito/latest/developerguide/what-is-amazon-cognito.html)
- [Amplify vs amazon-cognito-identity-js vs AWS SDK](https://www.maxivanov.io/aws-cognito-amplify-vs-amazon-cognito-identity-js-vs-aws-sdk)
