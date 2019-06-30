import React, { Component } from 'react';
import styles from './BodyweightPage.module.scss';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { Link } from 'react-router-dom';
import data from '../../data/BodyweightData';

class BodyweightExerciseListItem extends Component {
  render() {
    const {id, name, image, difficulty, targetMusclegroups} = this.props;

    return (
      <Link to={`/bodyweight/exercises/${id}`}  className={styles['ListItem']}>
        <img style={{height: 220, width: 440}} src={image} alt="Exercise Image" />
        <div className={styles['ListItemTextSection']}>
          <div className={styles['ListItemTextSectionTitle']}>{name}</div>
          <div className={styles['ListItemTextSectionBody']}>
            <p>
              <FontAwesomeIcon icon="arrows-alt-h" /> {null}&nbsp;&nbsp;&nbsp;
              <FontAwesomeIcon icon="clock" /> {null}&nbsp;&nbsp;&nbsp;
              <FontAwesomeIcon icon="arrow-up" /> {null}&nbsp;&nbsp;&nbsp;
              <FontAwesomeIcon icon="arrow-down" /> {null}&nbsp;&nbsp;&nbsp;
              <FontAwesomeIcon icon="layer-group" /> {null}
            </p>
          </div>
        </div>
      </Link>
    );
  }
}

class BodyweightWorkoutListItem extends Component {
  render() {
    const {id, name, image, difficulty, duration, targetMusclegroups} = this.props;

    return (
      <Link to={`/bodyweight/workouts/${id}`}  className={styles['ListItem']}>
        <img style={{height: 220, width: 440}} src={image} />
        <div className={styles['ListItemTextSection']}>
          <div className={styles['ListItemTextSectionTitle']}>{name}</div>
          <div className={styles['ListItemTextSectionBody']}>
            <p>
              <FontAwesomeIcon icon="arrows-alt-h" /> {null}&nbsp;&nbsp;&nbsp;
              <FontAwesomeIcon icon="clock" /> {null}&nbsp;&nbsp;&nbsp;
              <FontAwesomeIcon icon="arrow-up" /> {null}&nbsp;&nbsp;&nbsp;
              <FontAwesomeIcon icon="arrow-down" /> {null}&nbsp;&nbsp;&nbsp;
              <FontAwesomeIcon icon="layer-group" /> {null}
            </p>
          </div>
        </div>
      </Link>
    );
  }
}

class BodyweightPage extends Component {

  constructor(props) {
    super(props);
    this.state = {
      filterSectionExpanded: false,
      displayType: 'EXERCISES',
      duration: 120,
      difficulty: {
        easy: true,
        medium: true,
        hard: true
      },
      muscleGroups: {
        abs: true,
        biceps: true,
        calves: true,
        chest: true,
        forearm: true,
        glutes: true,
        lowerBack: true,
        shoulder: true,
        triceps: true,
        upperBack: true,
        upperLeg: true
      }
    };
  }

  toggleFilterSection = () => {
    this.setState((prevState) => ({
      ...prevState,
      filterSectionExpanded: !prevState.filterSectionExpanded
    }));
  };

  setDisplayType = (displayType) => {
    this.setState((prevState) => ({
      ...prevState,
      displayType: displayType
    }));
  };

  toggleMuscleGroup = (evt) => {
    const { value } = evt.target;

    this.setState((prevState) => ({
      ...prevState,
      muscleGroups: {
        ...prevState.muscleGroups,
        [value]: !prevState.muscleGroups[value]
      }
    }));
  };

  toggleDifficultyFilterGroup = (evt) => {
    const { value } = evt.target;

    this.setState((prevState) => ({
      ...prevState,
      difficulty: {
        ...prevState.difficulty,
        [value]: !prevState.difficulty[value]
      }
    }));
  };

  muscleGroupFilter = (exercise) => {
    const muscleGroups = Object.keys(this.state.muscleGroups)
      .filter(muscleGroup => this.state.muscleGroups[muscleGroup])
      .map(muscleGroup => muscleGroup.toUpperCase());

    for (let index in exercise.muscleGroups) {
      if (muscleGroups.includes(exercise.muscleGroups[index])) {
        return true;
      }
    }

    return false;
  };

  difficultyFilter = (exercise) => {
    const { easy, medium, hard } = this.state.difficulty;

    return (
      (easy && exercise.difficulty === 1) ||
      (medium && exercise.difficulty === 2) ||
      (hard && exercise.difficulty === 3)
    );
  };

  formatDuration = (durationInMinutes) => {
    const hours = Math.floor(durationInMinutes / 60);
    const minutes = durationInMinutes - hours * 60;

    if (hours > 0 && minutes === 0) {
      return `${hours}h`;
    }

    if (hours > 0) {
      return `${hours}h ${minutes}min`;
    }

    return `${minutes}min`;
  };

  durationFilterChange = (evt) => {
    const { value } = evt.target;
    this.setState(prevState => ({
      ...prevState,
      duration: value
    }));
  };

  render() {
    const { filterSectionExpanded, displayType, muscleGroups, difficulty } = this.state;

    return (
      <div className={styles['BodyweightPage']} style={{background: 'url(\'/bg.jpg\') no-repeat center center fixed', backgroundSize: 'cover'}}>
        <div className={styles['TextSection']} id="textSection">
          <h1>Bodyweight</h1>
        </div>
        <div className={styles['FilterSectionHeader']} onClick={this.toggleFilterSection}>
          <div style={{float: 'left'}}>Filter Bodyweight Exercises</div>
          <div style={{float: 'right'}}>
            <FontAwesomeIcon icon={filterSectionExpanded ? 'caret-up' : 'caret-down'} />
          </div>
        </div>
        <div className={styles['FilterSectionBody']} style={{height: this.state.filterSectionExpanded ? 240 : 0, padding: this.state.filterSectionExpanded ? 16 : null}}>
          <table className={styles['FilterTable']}>
            <tbody>
            <tr>
              <td scope="row">Toggle Exercises / Workouts</td>
              <td>
                <input type="radio" name="toggleType" checked={displayType === 'EXERCISES'} onClick={this.setDisplayType.bind(null, 'EXERCISES')} /> Exercises&nbsp;&nbsp;
                <input type="radio" name="toggleType" checked={displayType === 'WORKOUTS'} onClick={this.setDisplayType.bind(null, 'WORKOUTS')} /> Workouts
              </td>
            </tr>
            <tr>
              <td scope="row">Duration ({this.formatDuration(this.state.duration)})</td>
              <td><input type="range" min="5" max="180" value={this.state.duration} onChange={this.durationFilterChange} /></td>
            </tr>
            <tr>
              <td scope="row">Difficulty</td>
              <td>
                <input type="checkbox" name="difficulty" value="easy" checked={difficulty.easy} onChange={this.toggleDifficultyFilterGroup} /> Easy&nbsp;&nbsp;
                <input type="checkbox" name="difficulty" value="medium" checked={difficulty.medium} onChange={this.toggleDifficultyFilterGroup} /> Medium&nbsp;&nbsp;
                <input type="checkbox" name="difficulty" value="hard" checked={difficulty.hard} onChange={this.toggleDifficultyFilterGroup} /> Hard&nbsp;&nbsp;
              </td>
            </tr>
            <tr>
              <td scope="row">Muscle Groups</td>
              <td>
                <input type="checkbox" name="muscleGroups" value="abs" checked={muscleGroups.abs} onChange={this.toggleMuscleGroup} /> Abs&nbsp;&nbsp;
                <input type="checkbox" name="muscleGroups" value="biceps" checked={muscleGroups.biceps} onChange={this.toggleMuscleGroup} /> Biceps&nbsp;&nbsp;
                <input type="checkbox" name="muscleGroups" value="calves" checked={muscleGroups.calves} onChange={this.toggleMuscleGroup} /> Calves&nbsp;&nbsp;
                <input type="checkbox" name="muscleGroups" value="chest" checked={muscleGroups.chest} onChange={this.toggleMuscleGroup} /> Chest&nbsp;&nbsp;
                <input type="checkbox" name="muscleGroups" value="forearm" checked={muscleGroups.forearm} onChange={this.toggleMuscleGroup} /> Forearm&nbsp;&nbsp;
                <input type="checkbox" name="muscleGroups" value="glutes" checked={muscleGroups.glutes} onChange={this.toggleMuscleGroup} /> Glutes&nbsp;&nbsp;
                <input type="checkbox" name="muscleGroups" value="lowerBack" checked={muscleGroups.lowerBack} onChange={this.toggleMuscleGroup} /> Lower Back&nbsp;&nbsp;
                <input type="checkbox" name="muscleGroups" value="shoulder" checked={muscleGroups.shoulder} onChange={this.toggleMuscleGroup} /> Shoulder&nbsp;&nbsp;
                <input type="checkbox" name="muscleGroups" value="triceps" checked={muscleGroups.triceps} onChange={this.toggleMuscleGroup} /> Triceps&nbsp;&nbsp;
                <input type="checkbox" name="muscleGroups" value="upperBack" checked={muscleGroups.upperBack} onChange={this.toggleMuscleGroup} /> Upper Back&nbsp;&nbsp;
                <input type="checkbox" name="muscleGroups" value="upperLeg" checked={muscleGroups.upperLeg} onChange={this.toggleMuscleGroup} /> Upper Leg&nbsp;&nbsp;
              </td>
            </tr>
            </tbody>
          </table>
        </div>
        <div className={styles['ListSection']}>
          {
            displayType === 'EXERCISES' ?
              data.exercises
                .filter(exercise => this.difficultyFilter(exercise))
                .filter(exercise => this.muscleGroupFilter(exercise))
                .map((exercise) =>
              <BodyweightExerciseListItem
                id={exercise.id}
                image={exercise.image}
                name={exercise.name}
                difficulty={exercise.difficulty}
                targetMusclegroups={exercise.muscleGroups}
              />
            ) :
              data.workouts.map((workout) =>
                <BodyweightWorkoutListItem
                  id={workout.id}
                  image={workout.image}
                  name={workout.name}
                  difficulty={workout.difficulty}
                  targetMusclegroups={workout.muscleGroups}
                  duration={workout.duration}
                />
            )
          }
        </div>
      </div>
    );
  }
}

export default BodyweightPage;
