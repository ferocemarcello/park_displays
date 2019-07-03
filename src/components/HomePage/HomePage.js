import React, { Component } from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { Link } from 'react-router-dom';
import styles from './HomePage.module.scss';
import Glide from '@glidejs/glide';
import RunWalkData from '../../data/RunWalkData';
import BodyweightData from '../../data/BodyweightData';

class CircleBar extends Component {
  render() {
    const { value, maxValue } = this.props;
    return (
      <span>
        {
          [...new Array(value)].map((_, i) => <FontAwesomeIcon icon="circle" className={styles['CircleProgressDarkGrey']} key={i} />)
        }
        {
          (maxValue - value) > 0 ?
            [...new Array(maxValue - value)].map((_, i) => <FontAwesomeIcon icon="circle"  className={styles['CircleProgressLightGrey']} key={i} />) : null
        }
      </span>
    );
  }
}

class SliderItem extends Component {
  render() {
    const { title, text, difficulty, duration, linkTo } = this.props;
    return (
      <li className={`glide__slide ${styles['SliderItem']}`} style={{width: 200}}>
        <Link to={linkTo}>
          <div style={{padding: 16}}>
            <div>{title}</div>
            <div style={{color: 'darkgrey', fontSize: '.9rem', fontFamily: '"Helvetica Neue", Helvetica, Arial, sans-serif'}}>
              <span dangerouslySetInnerHTML={{__html: text}}></span>
              <hr />
              <div style={{display: 'flex', justifyContent: 'space-between'}}>
                <div><small>Duration: <CircleBar value={+duration} maxValue={3} /></small></div>
                <div><small>Difficulty: <CircleBar value={+difficulty} maxValue={3} /></small></div>
              </div>
            </div>
          </div>
        </Link>
      </li>
    );
  }
}

class Slider extends Component {
  render() {
    const { children, sliderId } = this.props;

    return (
      <div className={`glide glide${sliderId}`}>
        <div className="glide__track" data-glide-el="track">
          <ul className="glide__slides" style={{listStyle: 'none'}}>
            { children }
          </ul>
        </div>
      </div>
    );
  }

  componentDidMount() {
    new Glide(`.glide${this.props.sliderId}`, {
      type: 'slider',
      startAt: 0,
      perView: 5,
      focusAt: 'center',
      slideWidth: 300
    }).mount();
  }
}

class ShowAllLink extends Component {
  render() {
    return (
      <div style={{float: 'right', marginTop: 16}}>
        <Link to={this.props.to} style={{color: '#fff', textDecoration: 'none'}}>Show All <FontAwesomeIcon icon="chevron-right" /></Link>
      </div>
    );
  }
}

class HomePage extends Component {

  navigate = (to) => {
    this.props.history.push(to);
  };

  render() {
    return (
      <div className={styles['HomePage']}>
        <section className={styles['RunningSection']} onClick={this.navigate.bind(null, '/runwalk')}>
          <div>
            <div className={styles['SectionTitle']}>Running / Walking</div>
            <div className={styles['SectionDescription']}>Routes for walking</div>
            {/*<Slider sliderId={1}>
              { RunWalkData.map((track, i) => i > 12 ? null : <SliderItem key={i} title={track.name} text="" difficulty="1" duration="1" linkTo={`/runwalk/track/${track.id}`} />) }
            </Slider>
            <ShowAllLink to="/runwalk" />*/}
          </div>
        </section>
        <section className={styles['BodyweightSection']} onClick={this.navigate.bind(null, '/bodyweight')}>
          <div>
            <div className={styles['SectionTitle']}>Bodyweight</div>
            <div className={styles['SectionDescription']}>Powerful Workouts</div>
            {/*<Slider sliderId={2}>
              { BodyweightData.exercises.map((exercise, i) => i > 12 ? null : <SliderItem key={i} title={exercise.name} text="" difficulty={exercise.difficulty} duration="1" linkTo={`/bodyweight/exercises/${exercise.id}`} />) }
            </Slider>
            <ShowAllLink to="/bodyweight" />*/}
          </div>
        </section>
        <section className={styles['GymSection']} onClick={this.navigate.bind(null, '/gym')}>
          <div>
            <div className={styles['SectionTitle']}>Gym</div>
            <div className={styles['SectionDescription']}>Workouts with equipment</div>
            {/*<Slider sliderId={3}>
              { [...Array(13).keys()].map(i => <SliderItem key={i} title={`Gym Exercise ${i}`} text="This is a placeholder" difficulty="3" duration="1" />) }
            </Slider>
            <ShowAllLink to="/gym" />*/}
          </div>
        </section>
        <section className={styles['GroupFitnessSection']} onClick={this.navigate.bind(null, '/groupfitness')}>
          <div>
            <div className={styles['SectionTitle']}>Group Fitness</div>
            <div className={styles['SectionDescription']}>Community powered Workouts</div>
            {/*<Slider sliderId={4}>
              { [...Array(13).keys()].map(i => <SliderItem key={i} title={`Group Exercise ${i}`} text="This is a placeholder" difficulty="3" duration="1" />) }
            </Slider>
            <ShowAllLink to="/groupfitness" />*/}
          </div>
        </section>
        {
          /*
          <section className={styles['NutritionSection']}>
          <div>
            <div className={styles['SectionTitle']}>Nutrition</div>
            <div className={styles['SectionDescription']}>Find places to fuel up after workout</div>
            <Slider sliderId={5}>
              { [...Array(13).keys()].map(i => <SliderItem key={i} title={`Exercise ${i}`} text="This is the body Text<br/>it can have multiple lines" difficulty="3" duration="1" />) }
            </Slider>
            <ShowAllLink to="/nutrition" />
          </div>
        </section>
           */
        }
      </div>
    )
  }
}

export default HomePage;