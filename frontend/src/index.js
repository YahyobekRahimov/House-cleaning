import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import { ShortStateProvider } from "./hooks/shortState";
import { LongStateProvider } from "./hooks/longState";



const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <LongStateProvider> {/*THIS SUPPIES US WITH LONG TIME STATE*/}
			<ShortStateProvider> {/*THIS SUPPIES US WITH SHORT TIME STATE... READ BELOW DOWN*/}
				<App />
			</ShortStateProvider>
		</LongStateProvider>
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();



// ----------------> HEY, READ FROM HERE FOR UNDERSTANDING THE STATE PROVIDERS ABOVE:
// YOU CAN USE THESE STATE PROVIDERS IN ANY COMPONENT YOU WANT. BUT KEEP IN MIND THAT EVERY TIME SOMETHING CHANGES IN THESE STATES THE COMPONENTS THAT USES THESE STATES WILL BE RERENDERED!

// THIS MEANS TRY TO USE LESS THEM TO NOT SLOW DOWN THE APP BY RERENDERING ALL COMPONENTS FOR A SMALL CHANGE IN STATES.

// I LEFT YOU SOME COMMENT IN longState and shortState hook files to avoid from having very global providers to have specific component supplying providers. find hooks folder...