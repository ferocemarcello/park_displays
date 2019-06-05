import React, { Component } from 'react';
import { Link } from 'react-router-dom';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import styles from './ToolBarItem.module.scss';

class ToolBarItem extends Component {
  render() {
    const { icon, text, onClick } = this.props;

    return (
      <div className={styles['ToolBarItem']} onClick={onClick}>
        <span className={styles['ToolBarItemIcon']}>
          <FontAwesomeIcon icon={icon} />
        </span>
        {text ? <span className={styles['ToolBarItemText']}>{text}</span> : null}
      </div>
    )
  }
}

export default ToolBarItem;