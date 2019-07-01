import React from 'react';
import ReactDOM from 'react-dom';
import { library } from '@fortawesome/fontawesome-svg-core';
import {
  faArrowDown,
  faArrowLeft, faArrowsAltH, faArrowUp, faCaretDown, faCaretUp,
  faChevronRight, faCircle, faClock, faDumbbell, faHome, faLayerGroup,
  faMap,
  faMedkit,
  faPlus,
  faSun,
  faTimes, faTrophy,
  faUserCircle
} from '@fortawesome/free-solid-svg-icons';
import './index.scss';
import App from './containers/App';
import * as serviceWorker from './serviceWorker';
import { faFacebook, faGoogle, faStrava } from '@fortawesome/free-brands-svg-icons';

library.add([
  faUserCircle,
  faSun,
  faMap,
  faPlus,
  faMedkit,
  faArrowLeft,
  faTimes,
  faStrava,
  faFacebook,
  faGoogle,
  faChevronRight,
  faArrowsAltH,
  faClock,
  faArrowUp,
  faArrowDown,
  faLayerGroup,
  faCaretDown,
  faCaretUp,
  faCircle,
  faTrophy,
  faHome,
  faDumbbell
]);

ReactDOM.render(<App />, document.getElementById('root'));

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();
