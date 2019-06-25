import React, { Component } from 'react';
import styles from './DoWorkoutPage.module.scss';

class DoWorkoutPage extends Component {
  render() {
    return (
      <div>Do Workout Page - Workout ID: {this.props.match.params.workoutId} - Type: {this.props.match.params.workoutType}</div>
    );
  }
}

export default DoWorkoutPage;
