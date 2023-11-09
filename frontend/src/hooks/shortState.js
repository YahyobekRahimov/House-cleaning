import React, { createContext, useReducer, useContext } from 'react';

// Define the initial state
// THE DEFAULT STATE OBJECT IS TAKEN WHEN APPSTATE IS DEFINED IN LOCALSTORAGE
// YOU CAN STORE YOUR DATA HERE. 
// I THINK YOU SHOULD INCLUDE YOUR STORED ITEM IN THIS LIST
// THIS HELPS FOR EFFICIENCY AND BETTER UNDERSTANDING
const initialState = {
  // navActive: 'about', 
  // processMenuActive: 'daily',
  // processChartViewMode: 'bar',
  // processRangeSelected: 'All',
  // processMonthsSelected: ['All'],
  // processTypesSelected: ['All'],
  // singleTaskOpen: false,
  // tasksViewMode: 'mine',
  // taskOpened: 0,
  // tasksFilters: 'All',
  // tasksSortBy: "To'g'ri"


  // ... WRITE YOUR OWN
  // THIS IS SHORT STATE SUPPLIER WHICH CAN KEEP DATA FOR SHORT TIME! FOR EXAMPLE EVERY TIME THE PAGE REFRESHED THE INITIAL STATE (DATA IN THIS LIST) WILL BE SET
  };

// Define the reducer function
function reducer(state, action) {
  return {...state, ...action}
}

// Create the context
const ShortStateContext = createContext();

// Create a custom hook to access the state and dispatch
export function useShortState() {

  // YOU MUST KNOW THAT YOU CAN CREATE YOUR OWN STATE PROVIDER LIKE THIS AND WRAP YOUR HAPPY COMPONENTS WITH YOUR NEW STATEPROVIDER... REALLY WANT? COPY THE FILE AND PUT IT IN HOOKS FOLDER AND MAKE CHANGES: 
  // 1. find "useShortState" namings in code
  // 2. change 'useShortState' (the hook name) to your own
  // 3. enjoy your new hook!
  return useContext(ShortStateContext);
}

// Create the provider component
export function ShortStateProvider({ children }) {
  const [shortState, shortDispatch] = useReducer(reducer, initialState);

  return (
    <ShortStateContext.Provider value={{ shortState, shortDispatch }}>
      {children}
    </ShortStateContext.Provider>
  );
}
