import React, { Component } from 'react';
import { Link } from 'react-router-dom';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import styles from './ToolBarItem.module.scss';

class ToolBarItem extends Component {
  render() {
    const { icon, text, to } = this.props;

    return (
      <Link className={styles['ToolBarItem']} to={to}>
        <span className={styles['ToolBarItemIcon']}>
          <FontAwesomeIcon icon={icon} />
        </span>
        {text ? <span className={styles['ToolBarItemText']}>{text}</span> : null}
      </Link>
    )
  }
}

export default ToolBarItem;