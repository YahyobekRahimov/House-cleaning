import React, { createContext, useContext, useReducer } from 'react';

// THE DEFAULT STATE OBJECT IS TAKEN WHEN APPSTATE IS DEFINED IN LOCALSTORAGE
// YOU CAN STORE YOUR DATA HERE. 
// I THINK YOU SHOULD INCLUDE YOUR STORED ITEM IN THIS LIST
// THIS HELPS FOR EFFICIENCY AND BETTER UNDERSTANDING
const defaultState = JSON.parse(localStorage.getItem('appState')) || { // FIND 'appState BELOW'
  navActive: 'about', 
};
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


  // ... WRITE YOUR OWN HERE
  // THIS IS LONGSTATE WHICH CAN STORE DATA FOR LONG TIME. EVEN PAGE IS RENDERED AND IN SOME CASES EVEN THE DEVICE RESTARTED THE DATA IN THIS STATE PROVIDER IS KEPT AND FRESH. DO NOT SAVE PERSONAL AND SECRET DATA IN HERE. EVERYONE CAN SEE DATA OF LOCALSTORAGE.
const LongStateContext = createContext();

export function useLongState() {
  return useContext(LongStateContext);
}

const reducer = (state, action) => {
  console.log(state, action)
  const newState = {...state, ...action};
  console.log(newState)
  localStorage.setItem('appState', JSON.stringify(newState)); // YES, IT IS HERE. YOU MUST KNOW THAT YOU CAN CREATE YOUR OWN STATE PROVIDER LIKE THIS AND WRAP YOUR HAPPY COMPONENTS WITH YOUR NEW STATEPROVIDER. IF YOU DO, DO NOT FORGET TO SET DIFFERENT NAME TO STORE IN LOCALSTORAGE: OTHER THAN 'appState'. REALLY WANT? COPY THE FILE AND PUT IT IN HOOKS FOLDER AND MAKE CHANGES: 
  // 1. change 'appState' with your own
  // 2. change 'useLongState' (the hook name) to your own
  // 3. enjoy your new hook!
  return newState
};


export function useLongStateProvider() {
  const [longState, longDispatch] = useReducer(reducer, defaultState);
  return { longState, longDispatch };
}

export function LongStateProvider({ children }) {
  const stateProvider = useLongStateProvider();

  return (
    <LongStateContext.Provider value={stateProvider}>
      {children}
    </LongStateContext.Provider>
  );
}
