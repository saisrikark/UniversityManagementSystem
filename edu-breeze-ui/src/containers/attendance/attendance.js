import React from 'react';

import { CardTitle, CardText } from 'react-bootstrap/Card';
import Card from 'react-bootstrap/Card'
import Navbar from 'react-bootstrap/Navbar'
import Nav from 'react-bootstrap/Nav'
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';

import CardDeck from 'react-bootstrap/CardDeck'
import './attendance.css';
import { Component } from 'react';
import { connect } from 'react-redux';
import Container from 'react-bootstrap/Container';


class Attendance extends Component {
  constructor(props) {
    super(props);

    this.state = {
      isPageLoading: true,
    };
  }

  render() {
    return (
      <>
        <Navbar bg="dark" variant="dark" expand="lg" sticky="top">
          <Container>
            <Navbar.Brand href="#">EduBreeze</Navbar.Brand>
            <Navbar.Toggle aria-controls="responsive-navbar-nav" />
          </Container>

          <Navbar.Collapse id="responsive-navbar-nav">
            <Nav className="mr-auto">
              <Nav.Link href="/login">Logout</Nav.Link>
              <Nav.Link href="/dashboard">Dashboard</Nav.Link>
              <Nav.Link href="#pricing">Contact</Nav.Link>
            </Nav>
          </Navbar.Collapse>

        </Navbar>
        <br></br>
        <br></br>
        <h3>Your attendance details</h3>
        <br></br>
        <br></br>
        <Row>
          <Col sm="6">
            <Card body>
              <Card.Title>Object Oriented Modelling and Design</Card.Title>
              <br></br>
              <Card.Text>Classes Missed</Card.Text>
              <Card.Text><small>September - 7, 16</small></Card.Text>
              <Card.Text><small>October - 23, 29</small></Card.Text>
            </Card>
          </Col>
          <Col sm="6">
            <Card body>
              <Card.Title>Software Engineering</Card.Title>
              <Card.Text>Classes Missed</Card.Text>
              <Card.Text><small>September - 4, 17, 26</small></Card.Text>
            </Card>
          </Col>
        </Row>

        <Row>
          <Col sm="6">
            <Card body>
              <Card.Title>Web Technologies II</Card.Title>
              <Card.Text>Classes Missed</Card.Text>
              <Card.Text><small>September - 8, 13</small></Card.Text>
            </Card>
          </Col>
          <Col sm="6">
            <Card body>
              <Card.Title>Software Network Analysis</Card.Title>
              <Card.Text>Classes Missed</Card.Text>
              <Card.Text><small>November - 2, 17</small></Card.Text>
            </Card>
          </Col>
        </Row>

      </>
    );
  }
}


export default Attendance;



