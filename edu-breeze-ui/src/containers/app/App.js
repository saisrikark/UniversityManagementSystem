import React from 'react';
import './App.css';
import Home from '../home/home.js';
import { Route } from 'react-router-dom';
import Login from '../login';
import Dashboard from './../dashboard';
import Assignment from '../assignment/assignment.js';
import Attendance from '../attendance/attendance.js';
import Blog from '../blog/blog.js';
import Material from '../material/material.js';

function App() {
  return (
    <main>
      <Route exact path="/" component={Home} />
      <Route exact path="/login" component={Login} />
      <Route path="/dashboard" component={Dashboard} />
      <Route path="/assignment" component={Assignment} />
      <Route path="/attendance" component={Attendance} />
      <Route path="/blog" component={Blog} />
      <Route path="/material" component={Material} />
    </main>
  );
}

export default App;
