import React, { Component } from 'react';
import styles from './BodyweightExerciseDetailPage.module.scss';
import BodyweightData from '../../data/BodyweightData';

class BodyweightExerciseDetailPage extends Component {
  render() {
    const exercise = BodyweightData.exercises.filter(exercise => exercise.id == this.props.match.params.exerciseId)[0];


    return (
      <div className={styles['BodyweightExerciseDetailPage']}>
        <section className={styles['TextSection']}>
          <h2>Bodyweight Exercise</h2>
          <h1>{exercise.name}</h1>

        </section>
      </div>
    );
  }
}

export default BodyweightExerciseDetailPage;
