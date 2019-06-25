import React, { Component } from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { Link } from 'react-router-dom';
import styles from './HomePage.module.scss';
import Glide from '@glidejs/glide';

class SliderItem extends Component {
  render() {
    const { title, text, difficulty, duration } = this.props;

    return (
      <li className="glide__slide" style={{background: 'white', color: 'black', fontSize: '1.2rem'}}>
        <div style={{padding: 16}}>
          <div>{title}</div>
          <div style={{color: 'darkgrey', fontSize: '.9rem', fontFamily: '"Helvetica Neue", Helvetica, Arial, sans-serif'}}>
            <span dangerouslySetInnerHTML={{__html: text}}></span>
            <hr />
            <div style={{display: 'flex', justifyContent: 'space-between'}}>
              <div><small>Duration: {duration}/3</small></div>
              <div><small>Difficulty: {difficulty}/3</small></div>
            </div>
          </div>
        </div>
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
      focusAt: 'center'
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
  render() {
    return (
      <div className={styles['HomePage']}>
        <section className={styles['RunningSection']}>
          <div>
            <div className={styles['SectionTitle']}>Running / Walking</div>
            <div className={styles['SectionDescription']}>Routes for walking</div>
            <Slider sliderId={1}>
              { [...Array(13).keys()].map(i => <SliderItem key={i} title={`Exercise ${i}`} text="This is the body Text<br/>it can have multiple lines" difficulty="3" duration="1" />) }
            </Slider>
            <ShowAllLink to="/runwalk" />
          </div>
        </section>
        <section className={styles['BodyweightSection']}>
          <div>
            <div className={styles['SectionTitle']}>Bodyweight</div>
            <div className={styles['SectionDescription']}>Powerful Workouts</div>
            <Slider sliderId={2}>
              { [...Array(13).keys()].map(i => <SliderItem key={i} title={`Exercise ${i}`} text="This is the body Text<br/>it can have multiple lines" difficulty="3" duration="1" />) }
            </Slider>
            <ShowAllLink to="/bodyweight" />
          </div>
        </section>
        <section className={styles['GymSection']}>
          <div>
            <div className={styles['SectionTitle']}>Gym</div>
            <div className={styles['SectionDescription']}>Workouts with equipment</div>
            <Slider sliderId={3}>
              { [...Array(13).keys()].map(i => <SliderItem key={i} title={`Exercise ${i}`} text="This is the body Text<br/>it can have multiple lines" difficulty="3" duration="1" />) }
            </Slider>
            <ShowAllLink to="/gym" />
          </div>
        </section>
        <section className={styles['GroupFitnessSection']}>
          <div>
            <div className={styles['SectionTitle']}>Group Fitness</div>
            <div className={styles['SectionDescription']}>Community powered Workouts</div>
            <Slider sliderId={4}>
              { [...Array(13).keys()].map(i => <SliderItem key={i} title={`Exercise ${i}`} text="This is the body Text<br/>it can have multiple lines" difficulty="3" duration="1" />) }
            </Slider>
            <ShowAllLink to="/groupfitness" />
          </div>
        </section>
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
      </div>
    )
  }

  componentDidMount() {
    /*new Glide('.glide1', {
      type: 'slider',
      startAt: 0,
      perView: 5,
      focusAt: 'center'
    }).mount();

    new Glide('.glide2', {
      type: 'slider',
      startAt: 0,
      perView: 5,
      focusAt: 'center'
    }).mount();

    new Glide('.glide3', {
      type: 'slider',
      startAt: 0,
      perView: 5,
      focusAt: 'center'
    }).mount();

    new Glide('.glide4', {
      type: 'slider',
      startAt: 0,
      perView: 5,
      focusAt: 'center'
    }).mount();

    new Glide('.glide5', {
      type: 'slider',
      startAt: 0,
      perView: 5,
      focusAt: 'center'
    }).mount();*/
  }
}

export default HomePage;