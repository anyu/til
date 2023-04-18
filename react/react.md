# React

## React Hooks
React 16.8 introduced Hooks, enabling using state without a separate class.

### Rules of Hooks
- Only call Hooks at the top level in the body of a function component or custom Hook, before early returns.
- Don't call Hooks inside loops, conditions, nested functions
  - This ensures that Hooks are called in the same order each time a component renders, which lets React correctively preserve state of Hooks between multiple `useState` and `useEffect` calls
  - If needed, extract a new component and move the state into it.
- Only Call Hooks from React funcs, not JS funs

### State Hooks
- [useState](https://react.dev/reference/react/useState): the first tool to reach for for simple local state

  ```js
  import { useState } from "react";

  function Layout() {
    const [isSidebarOpen, setSidebarOpen] = useState(false);

    return (
      <>
        <Sidebar isSidebarOpen={isSidebarOpen} closeSidebar={() => setSidebarOpen(false)} />
        {/* ... */}
      </>
    );
  ```
- [useReducer](https://react.dev/reference/react/useReducer#reference): Similar to `useState` but instead of an initial state, it accepts a reducer function (function that specifies how the state gets updated. Takes in the state and action, and returns the next state)
  - The `dispatch` function returned by `useReducer` only updates the state variable for the *next render*. If you read the state variable after calling the dispatch function, you'll still get the old value from before the call.
  - Can be used for local or global state
  - Pros: provides a built-in way to perform different state operations with the help of the reducer function
  - Useful if you have a complicated state that you want to make sure all update logic is in a centralized location
  
    ```js
    const initialState = { votes: 0 };

    function reducer(state, action) {
      switch (action.type) {
        case 'upvote':
          return {votes: state.votes + 1};
        case 'downvote':
          return {votes: state.votes - 1};
        default:
          throw new Error();
      }
    }

    function VoteCounter() {
      const [state, dispatch] = useReducer(reducer, initialState);

      return (
        <>
          Current Votes: {state.votes}
          <button onClick={() => dispatch({type: 'upvote'})}>Upvote</button>
          <button onClick={() => dispatch({type: 'downvote'})}>Downvote</button>
        </>
      );
    }
    ```

### Context Hooks
- [useContext](https://react.dev/reference/react/useContext): Lets a component receive info from distant parents without passing it as props. A way to avoid prop drilling (when you have to pass down props through intermediate components that don't need it)
- Not technically a state management solution to some
- Good for situations with static data that undergoes lower-frequency updates such as language/time/location prefs, user auth
- Cons: 
  - Default behavior is to re-render all children components if the value provided to it as a prop changes.
  - In many cases you don't want all children to update in response to a global state update (not all children may consume/rely on that state). You only want to re-runder if their props or state changes.
  - Bad practice to combine `useReducer` and `useContext`
- Best practice:
  - Try splitting large context into multiple contexts and keep state close to its component consumer.
- **Note**: In Strict Mode (development-only, not prod), React will call the reducer and initializer twice to help surface accidental impurities. 
  - The result from one of these calls is ignored, so shouldn't affect logic

### Ref Hooks
- [useRef](https://react.dev/reference/react/useRef): Lets a component hold some info that isn't used for rendering, like a DOM node or timeout ID.
- Unlike with state, updating a ref does **not** re-render your component. An 'escape hatch' from the Ract paradigm; useful for working with non-React systems, such as brower APIs.

### Effect Hooks
- [useEffect](https://react.dev/reference/react/useEffect): Lets a component connect to and sync with external systems, eg. network calls, DOM, animations, non-React code.
- Another 'escape hatch' from the React paradigm; don't use it to orchestrate data flow.
- If not interacting with an external system, may not need this

### Performance Hooks

Avoid unnecessary re-rendering and skip calculations:
- [useMemo](https://react.dev/reference/react/useMemo)
  - Cache result of an expensive calculation
- [useCallback](https://react.dev/reference/react/useCallback)
  - Cache a function definition before passing it down to an optimized component

In cases where you can't skip re-rendering, "prioritize rendering". Separate blocking updates that must be synchronous (eg. typing into an input) from non-blocking updates which don’t need to block  UI (eg. updating a chart):
- [useTransition](https://react.dev/reference/react/useTransition)
  - Update state w/o blocking UI
- [useDeferredValue](https://react.dev/reference/react/useDeferredValue)
  - Defer updating a part of the UI

## State Management

### Local state
- State only used in 1 or other component
- Lifting state up
  - Extracting state from two components to their parent, then passing down via props.
- Methods: State hooks  

### Global state
- State managed across components
- eg. authenticated user state
- Methods: Context hooks, libs below

### State Management Libs

| Name      | Highlights
| :------------- |:-------------
| [Redux](https://github.com/reduxjs/redux) | - Still the most widely used lib by far. <br/>- Heavy overhead
| [Redux Toolkit](https://github.com/reduxjs/redux-toolkit) | - Simplified, opinionated approach to using Redux. <br/> - Cons: Newer, less support.
| [MobX](https://github.com/mobxjs/mobx) | - Currently the 3rd most popular option after Context, Redux. <br/>- Uses OOP model and an observer/observable pattern. Continually monitors for changes and re-renders as data is manipulated.<br/>- Good community support.
| [Zustand](https://github.com/pmndrs/zustand) | -  Perhaps the smallest lib, simple and minimal API based on hooks, fast/scalable. Components don't need to be wrapped in a Context Provider.
| [Jotai](https://jotai.org/) | - Small, cleaner API, good TS support, deeper maturity, very performant due to GC implementation
| [Hookstate](https://github.com/avkonst/hookstate) | - A modern, minimal yet scalable lib. Virtually no boilerplate<br/>- TS-first lib<br/>- Supports plugins<br/>- Unique in how it tracks/updates state<br/>- Cons: Newer lib, so smaller community
| [Recoil](https://github.com/facebookexperimental/Recoil) | - Experimental lib form FB<br/>- Uses concepts of atoms/selectors<br/>- Supposedly easier to modify/maintain<br/>- Cons: New, small community, React-dependent
| [Xstate](https://github.com/statelyai/xstate) | - State-machine based lib. Constrains possible states to avoid impossible state situations<br/>- Seems to be good for a very particular use case (when data is modeled in a finite state machine), but less fitting for traditional web uses such as querying a backend.<br/>- Doesn't seem like a complete replacement for other state mgmt solutions.

### Server state
- Data from external servers that must be integrated with UI state
- [SWR](https://swr.vercel.app/) and [React Query](https://github.com/tanstack/query) can help with this, since this may be hard to manage alongside local and global UI state.

### URL state
- Data that exists on URLs (eg. path name, query params)

--- 

## CSS Management

--- 

## Component Management

--- 

## Performance
