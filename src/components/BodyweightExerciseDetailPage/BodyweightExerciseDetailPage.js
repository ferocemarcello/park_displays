import React, { Component } from 'react';
import styles from './BodyweightExerciseDetailPage.module.scss';

class BodyweightExerciseDetailPage extends Component {
  render() {
    return (
      <div>Bodyweight Exercise Detail Page - Exercise ID: {this.props.match.params.exerciseId}</div>
    );
  }
}

export default BodyweightExerciseDetailPage;
