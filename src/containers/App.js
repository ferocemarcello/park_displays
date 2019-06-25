import React, { Component } from 'react';
import { Router, Route } from 'react-router-dom';
import { createHashHistory } from 'history';
import './App.scss';
import ToolBar from '../components/toolbar/ToolBar';
import HomePage from '../components/HomePage/HomePage';
import EmergencyPage from '../components/EmergencyPage/EmergencyPage';
import ParkMapPage from '../components/ParkMapPage/ParkMapPage';
import WeatherForecastPage from '../components/WeatherForecastPage/WeatherForecastPage';
import ConnectModal from '../components/connectModal/ConnectModal';
import RunWalkPage from '../components/RunWalkPage/RunWalkPage';
import TrackDetailPage from '../components/TrackDetailPage/TrackDetailPage';
import BodyweightPage from '../components/BodyweightPage/BodyweightPage';
import BodyweightExerciseDetailPage from '../components/BodyweightExerciseDetailPage/BodyweightExerciseDetailPage';
import BodyweightWorkoutDetailPage from '../components/BodyweightWorkoutDetailPage/BodyweightWorkoutDetailPage';
import DoWorkoutPage from '../components/DoWorkoutPage/DoWorkoutPage';

const history = createHashHistory();

class App extends Component {

  constructor(props) {
    super(props);
    this.state = {
      connectModalOpen: false
    };
  }

  showConnectModal = () => {
    this.setState((prevState) => ({
      ...prevState,
      connectModalOpen: true
    }));
  };

  hideConnectModal = () => {
    console.log('hide modal')
    this.setState((prevState) => ({
      ...prevState,
      connectModalOpen: false
    }));
  };

  render() {
    const { connectModalOpen } = this.state;
    return (
      <div className="App">
        <Router history={history}>
          <main className="appContentWrapper">
            <Route path="/emergency" exact component={EmergencyPage} />
            <Route path="/map" exact component={ParkMapPage} />
            <Route path="/weather" exact component={WeatherForecastPage} />
            <Route path="/runwalk" exact component={RunWalkPage} />
            <Route path="/runwalk/track/:trackId" exact component={TrackDetailPage} />
            <Route path="/bodyweight/exercises/:exerciseId" exact component={BodyweightExerciseDetailPage} />
            <Route path="/bodyweight/workouts/:workoutId" exact component={BodyweightWorkoutDetailPage} />
            <Route path="/bodyweight" exact component={BodyweightPage} />
            <Route path="/workouts/:workoutType/:workoutId/do" exact component={DoWorkoutPage} />
            <Route path="/" exact component={HomePage} />
          </main>
          <ToolBar history={history} showConnectModal={this.showConnectModal} />
          { connectModalOpen ? <ConnectModal closeConnectModal={this.hideConnectModal} /> : null }
        </Router>
      </div>
    );
  }
}

export default App;
