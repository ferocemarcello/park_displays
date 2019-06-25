import React, { Component } from 'react';
import styles from './BodyweightPage.module.scss';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { Link } from 'react-router-dom';
import data from '../../data/BodyweightData';

class BodyweightExerciseListItem extends Component {
  render() {
    const {id, name, image, difficulty, targetMusclegroups} = this.props;

    return (
      <Link to={`/bodyweight/exercise/${id}`}  className={styles['ListItem']}>
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

class BodyweightWorkoutListItem extends Component {
  render() {
    const {id, name, image, difficulty, duration, targetMusclegroups} = this.props;

    return (
      <Link to={`/bodyweight/workout/${id}`}  className={styles['ListItem']}>
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
      displayType: 'EXERCISES'
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

  render() {
    const { filterSectionExpanded, displayType } = this.state;

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
        <div className={styles['FilterSectionBody']} style={{height: this.state.filterSectionExpanded ? 150 : 0, padding: this.state.filterSectionExpanded ? 16 : null}}>
          <p>
            <span>Show Exercises or Workouts</span>
            <span>
              <input type="radio" name="toggleType" checked={displayType === 'EXERCISES'} onClick={this.setDisplayType.bind(null, 'EXERCISES')} /> Exercises
              <input type="radio" name="toggleType" checked={displayType === 'WORKOUTS'} onClick={this.setDisplayType.bind(null, 'WORKOUTS')} /> Workouts
            </span>
          </p>
          <p>
            <span>Duration</span>
            <span>
              <input type="range" min="0" max="100" />
            </span>
          </p>
          <p>
            <span>Difficulty</span>
            <span>
              <input type="range" min="0" max="100" />
            </span>
          </p>
          <p>
            <span>Muscle Groups</span>
            <span>
              <input type="checkbox" name="groundType" /> Gravel
              <input type="checkbox" name="groundType" /> Grass
              <input type="checkbox" name="groundType" /> Asphalt
            </span>
          </p>
        </div>
        <div className={styles['ListSection']}>
          {
            displayType === 'EXERCISES' ?
              data.exercises.map((exercise) =>
              <BodyweightExerciseListItem
                id={exercise.id}
                image={null}
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
