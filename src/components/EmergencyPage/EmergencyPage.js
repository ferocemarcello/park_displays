import React, { Component } from 'react';
import styles from './EmergencyPage.module.scss';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';

class Step extends Component {
  render() {
    const { image, title, number, html } = this.props;

    return (
      <div className={styles['Step']}>
        <div className={styles['StepImageWrapper']}>
          <img className={styles['StepImage']} src={image}/>
          <div className={styles['StepLabel']}>{number}</div>
        </div>
        <div className={styles['StepContentSection']}>
          <h2>Open the Airway</h2>
          <span dangerouslySetInnerHTML={html}></span>
        </div>
      </div>
    );
  }
}

class EmergencyPage extends Component {
  constructor(props) {
    super(props);
    this.state = {
      step: 0,
      responsiveness: null,
      breathing: null
    };
  }

  setStep = (step, attribute, value) => {
    if (attribute) {
      this.setState(prevState => ({
        ...prevState,
        [attribute]: value,
        step: step
      }));
    } else {
      this.setState(prevState => ({
        ...prevState,
        step: step
      }));
    }
  };

  renderStep = (step) => {
    const { responsiveness, breathing } = this.state;

    if (step === 0) {
      return (
        <div className={styles['Step']}>
          <div className={styles['StepImageWrapper']}>
            <img className={styles['StepImage']} src="emergency/responsiveness.jpg" />
            <div className={styles['StepLabel']}>1</div>
          </div>
          <div className={styles['StepContentSection']}>
            <h2>Check for Responsiveness</h2>
            <p>Tap the shoulder and shout, “Are you OK?”</p>
            <p>
              Did the person react?
              <button className={responsiveness || responsiveness === null ? styles['YesButton'] : styles['GreyButton']} onClick={this.setStep.bind(null, 2, 'responsiveness', true)}>Yes</button>
              <button className={!responsiveness ? styles['NoButton'] : styles['GreyButton']} onClick={this.setStep.bind(null, 2, 'responsiveness', false)}>No</button>
            </p>
          </div>
        </div>
      );
    }

    if (step === 1 && !responsiveness) {
      return (
        <div className={styles['Step']}>
          <div className={styles['StepImageWrapper']}>
            <img className={styles['StepImage']} src="emergency/tilt_head.jpg" />
            <div className={styles['StepLabel']}>2</div>
          </div>
          <div className={styles['StepContentSection']}>
            <h2>Open the Airway</h2>
            <p>Tilt head, lift chin.</p>
          </div>
        </div>
      );
    }

    if (step === 1 && responsiveness) {
      return (
        <div className={styles['Step']}>
          <div className={styles['StepImageWrapper']}>
            <img className={styles['StepImage']} src="emergency/positioning.jpg" />
            <div className={styles['StepLabel']}>2</div>
          </div>
          <div className={styles['StepContentSection']}>
            <h2>Positioning</h2>
            <p>Help the person to find a comfortable position.</p>
            <p>Call 112 for medical assistance.</p>
          </div>
        </div>
      );
    }

    if (step === 2 && !responsiveness) {
      return (
        <div className={styles['Step']}>
          <div className={styles['StepImageWrapper']}>
            <img className={styles['StepImage']} src="emergency/check_breathing.jpg" />
            <div className={styles['StepLabel']}>3</div>
          </div>
          <div className={styles['StepContentSection']}>
            <h2>Check for Breathing</h2>
            <p>Check quickly for breathing for no more than 10 seconds.</p>
            <p>
              Does the person breath?
              <button className={breathing || breathing === null ? styles['YesButton'] : styles['GreyButton']} onClick={this.setStep.bind(null, 3, 'breathing', true)}>Yes</button>
              <button className={!breathing ? styles['NoButton'] : styles['GreyButton']} onClick={this.setStep.bind(null, 5, 'breathing', false)}>No</button>
            </p>
          </div>
        </div>
      );
    }

    if (step === 3 && !breathing) {
      return (
        <div className={styles['Step']}>
          <div className={styles['StepImageWrapper']}>
            <img className={styles['StepImage']} src="emergency/cpr.jpg" />
            <div className={styles['StepLabel']}>4</div>
          </div>
          <div className={styles['StepContentSection']}>
            <h2>Give 30 Chest compressions and call 112</h2>
            <p>Push hard, push fast in the middle of the
              chest at least <b>2</b> inches deep and at least
              <b>100</b> compressions per minute</p>
            <p>Ask people around to call 112.</p>
          </div>
        </div>
      );
    }

    if (step === 4 && !breathing) {
      return (
        <div className={styles['Step']}>
          <div className={styles['StepImageWrapper']}>
            <img className={styles['StepImage']} src="emergency/rescue_breaths.jpg" />
            <div className={styles['StepLabel']}>5</div>
          </div>
          <div className={styles['StepContentSection']}>
            <h2>Give 2 Rescue Breaths</h2>
            <ul>
              <li>Tilt the head back and lift the chin up.</li>
              <li>Pinch the nose shut then make a complete seal over the person’s mouth.</li>
              <li>Blow in for about 1 second to make the chest clearly rise.</li>
              <li>Give rescue breaths, one after the other.</li>
            </ul>
          </div>
        </div>
      );
    }

    if (step === 5 && !breathing) {
      return (
        <div className={styles['Step']}>
          <div className={styles['StepImageWrapper']}>
            <img className={styles['StepImage']} src="https://www.medizinus.info/wp-content/uploads/2015/10/defi-zeichen.png" />
            <div className={styles['StepLabel']}>6</div>
          </div>
          <div className={styles['StepContentSection']}>
            <h2>Do not stop</h2>
            Continue cycles of CPR (Step 4 &amp; 5). Do not stop CPR except in one of these situations<br />
            <ul>
              <li>You find an obvious sign of life, such as breathing.</li>
              <li>An AED is ready to use.</li>
              <li>Another trained responder or EMS personnel take over.</li>
              <li>You are too exhausted to continue.</li>
              <li>The scene becomes unsafe.</li>
            </ul>
          </div>
        </div>
      );
    }

    if (step === 3 && breathing) {
      return (
        <div className={styles['Step']}>
          <div className={styles['StepImageWrapper']}>
            <img className={styles['StepImage']} src="emergency/nato_positioning.jpg" />
            <div className={styles['StepLabel']}>4</div>
          </div>
          <div className={styles['StepContentSection']}>
            <h2>Recovery Position</h2>
            <p>Turn the person to the side as shown in the picture to the left.</p>
          </div>
        </div>
      );
    }
  };

  renderSteps = () => {
    const { step } = this.state;
    return [ ...new Array(step + 1).keys() ].map((_, index) => this.renderStep(index));
  };

  render() {
    return (
      <div className={styles['EmergencyPage']}>
        <section className={styles['TextSection']}>
          <h1>Emergency</h1>
          Step: {this.state.step}
          { this.renderSteps() }
        </section>
      </div>
    )
  }
}

export default EmergencyPage;