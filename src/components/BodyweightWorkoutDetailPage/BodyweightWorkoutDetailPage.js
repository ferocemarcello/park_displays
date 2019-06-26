import React, { Component } from 'react';
import { Link } from 'react-router-dom';
import styles from './BodyweightWorkoutDetailPage.module.scss';
import BodyweightData from '../../data/BodyweightData';

class BodyweightWorkoutDetailPage extends Component {
  render() {
    const workout = BodyweightData.workouts.filter(workout => workout.id == this.props.match.params.workoutId)[0];

    return (
      <div className={styles['BodyweightWorkoutDetailPage']}>
        <section className={styles['TextSection']}>
          <h2>Bodyweight Workout</h2>
          <h1>{workout.name}</h1>
          <Link to={`/workouts/bodyweight/${workout.id}/do`} className={styles['StartButton']}>Start Workout</Link>
          <h3>Important Information</h3>
          Exercises
          <h3>Overview</h3>
          {
            workout.rounds.map((round, i) => {
              return (
                <>
                <h4>Round {i + 1}/{workout.rounds.length}</h4>
                <table className={styles['ExerciseTable']}>
                  <tbody>
                    {
                      round.exercises.map(exercise => {
                        let ex = BodyweightData.exercises.filter(exerciseItem => exercise.exerciseId == exerciseItem.id)[0];
                        return (
                            <tr>
                              <td scope="row">{exercise.reps}x {ex.name}</td>
                            </tr>
                        );
                      })
                    }
                  </tbody>
                </table>
                </>
              )
            })
          }
        </section>
      </div>
    );
  }
}

export default BodyweightWorkoutDetailPage;
