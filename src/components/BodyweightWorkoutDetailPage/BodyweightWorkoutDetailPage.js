import React, { Component } from 'react';
import styles from './BodyweightWorkoutDetailPage.module.scss';

class BodyweightWorkoutDetailPage extends Component {
  render() {
    return (
      <div>Bodyweight Workout Detail Page - Workout ID: {this.props.match.params.workoutId}</div>
    );
  }
}

export default BodyweightWorkoutDetailPage;
