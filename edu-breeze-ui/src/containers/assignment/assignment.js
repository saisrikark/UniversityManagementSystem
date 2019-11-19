import React from 'react';
import { FilePond } from 'react-filepond';

import 'filepond/dist/filepond.min.css';

import { CardTitle, CardText } from 'react-bootstrap/Card';
import Card from 'react-bootstrap/Card'
import Navbar from 'react-bootstrap/Navbar'
import Nav from 'react-bootstrap/Nav'
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import Modal from 'react-bootstrap/Modal'
import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';

import CardDeck from 'react-bootstrap/CardDeck'
import './assignment.css';
import { Component } from 'react';
import { connect } from 'react-redux';
import Container from 'react-bootstrap/Container';


class Assignment extends Component {
  constructor(props) {
    super(props);

    this.state = {
      modalOpen: false,
      isPageLoading: true,
      files: [],
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
        <h3>You have the following assignments due</h3>
        <br></br>
        <br></br>
        <Row>
          <Col sm="4">
            <Card body>
              <Card.Title>Object Oriented Modelling and Design</Card.Title>
              <br></br>
              <Card.Text>Use Case Diagram</Card.Text>
              <Card.Text><small>Due 23rd November 2019</small></Card.Text>
              <Button onClick={e => this.setState({ modalOpen: true })}>Submit</Button>
            </Card>
          </Col>
          <Col sm="4">
            <Card body>
              <Card.Title>Software Engineering</Card.Title>
              <Card.Text>Requirements Specification</Card.Text>
              <Card.Text><small>Due 27th November 2019</small></Card.Text>
              <Button onClick={e => this.setState({ modalOpen: true })}>Submit</Button>
            </Card>
          </Col>

          <Col sm="4">
            <Card body>
              <Card.Title>Web Technologies II</Card.Title>
              <Card.Text>COMET</Card.Text>
              <Card.Text><small>Due 29th November 2019</small></Card.Text>
              <Button onClick={e => this.setState({ modalOpen: true })}>Submit</Button>
            </Card>
          </Col>
        </Row>

        <Modal
          show={this.state.modalOpen}
          size="lg"
          centered
          onHide={e => { this.setState({ modalOpen: false }) }}
        >
          <Modal.Header closeButton>
            <Modal.Title id="contained-modal-title-vcenter">
              Upload Assignment
        </Modal.Title>
          </Modal.Header>
          <Modal.Body>

            <FilePond
              server = "http://127.0.0.1:5002/submit"
              allowMultiple={true}
              onupdatefiles={(fileItems) => { this.setState({ files: fileItems.map(fileItem => fileItem.file) }); }}
            />
          </Modal.Body>
          <Modal.Footer>
            <Button onClick={e => { console.log(this.state) }}>Upload</Button>
          </Modal.Footer>
        </Modal>

      </>
    );
  }
}






export default Assignment;



