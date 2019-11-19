import React from 'react';
import {
  MDBCarousel,
  MDBCarouselCaption,
  MDBCarouselInner,
  MDBCarouselItem,
  MDBView,
  MDBMask,
} from "mdbreact";
import Navbar from 'react-bootstrap/Navbar'
import Nav from 'react-bootstrap/Nav'
import Container from 'react-bootstrap/Container'
import slide1 from './../../resources/slide1.jpg';
import slide2 from './../../resources/slide2.jpg';
import slide3 from './../../resources/slide3.jpg';
import './home.css';

const Home = () => {

  return (

    <>
      <Navbar expand="lg" sticky="top">
        <Container>
          <Navbar.Brand href="#">EduBreeze</Navbar.Brand>
        </Container>
        <Nav className="mr-auto">
          <Nav.Link href="/login">Login</Nav.Link>
          <Nav.Link href="/dashboard">Dashboard</Nav.Link>
          <Nav.Link href="#pricing">Contact</Nav.Link>
        </Nav>

      </Navbar>
      <MDBCarousel
        interval={3000}
        onHoverStop={true}
        activeItem={1}
        length={3}
        showControls={true}
        showIndicators={true}
        className="z-depth-1"
      >
        <MDBCarouselInner>
          <MDBCarouselItem itemId="1">
            <MDBView>
              <img
                className="d-block w-100"
                src={slide1}
                alt="slide1"
              />
              <MDBMask overlay="black-light" />
            </MDBView>
            <MDBCarouselCaption>
              <h3 className="h3-responsive">EduBreeze - One-stop Educational Institution Management</h3>

            </MDBCarouselCaption>
          </MDBCarouselItem>
          <MDBCarouselItem itemId="2">
            <MDBView>
              <img
                className="d-block w-100"
                src={slide2}
                alt="Second slide"
              />
              <MDBMask overlay="black-strong" />
            </MDBView>
            <MDBCarouselCaption>
              <h3 className="h3-responsive">Assignments. Checked!</h3>
              <p>Upload and submit assignments. Have them plagiarism checked. All in one place.</p>
            </MDBCarouselCaption>
          </MDBCarouselItem>
          <MDBCarouselItem itemId="3">
            <MDBView>
              <img
                className="d-block w-100"
                src={slide3}
                alt="Third slide"
              />
              <MDBMask overlay="black-slight" />
            </MDBView>
            <MDBCarouselCaption>
              <h3 className="h3-responsive">Placements made easy.</h3>
              <p>Find the right company, at the right time.</p>
            </MDBCarouselCaption>
          </MDBCarouselItem>
        </MDBCarouselInner>
      </MDBCarousel>
    </>

  );

}

export default Home;



