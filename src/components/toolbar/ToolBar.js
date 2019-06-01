import React, { Component } from 'react';
import './ToolBar.scss';
import ToolBarItem from '../toolbar-item/ToolBarItem';
import BackToolbarItem from '../toolbar-item/BackToolbarItem';

class ToolBar extends Component {
  render() {
    return (
      <div className="toolbar">
        <BackToolbarItem history={this.props.history} />
        <ToolBarItem text="Emergency" icon="medkit" to="/emergency" />
        <ToolBarItem text="Park Map" icon="map" to="/map" />
        <ToolBarItem text="Weather Forecast" icon="sun" to="/weather" />
        <ToolBarItem text="Connect" icon="user-circle" to="/login" />
      </div>
    )
  }
}

export default ToolBar;