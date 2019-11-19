import React from 'react';
import { FilePond } from 'react-filepond';
import 'quill/dist/quill.snow.css';
import 'filepond/dist/filepond.min.css';
import Quill from 'quill';
import { CardTitle, CardText } from 'react-bootstrap/Card';
import Card from 'react-bootstrap/Card'
import Navbar from 'react-bootstrap/Navbar'
import Nav from 'react-bootstrap/Nav'
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import Modal from 'react-bootstrap/Modal'
import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';
import DropdownButton from 'react-bootstrap/DropdownButton'
import Dropdown from 'react-bootstrap/Dropdown'
import CardDeck from 'react-bootstrap/CardDeck'
import './material.css';
import { Component } from 'react';
import { connect } from 'react-redux';
import Container from 'react-bootstrap/Container';


class Material extends Component {
    constructor(props) {
        super(props);

        this.state = {
            modalOpen: false,
            isPageLoading: true,
            files: [],
            materialCreate: false,
            materialRead: false,
        };

        this.onShowMaterial = this.onShowMaterial.bind(this);
    }

    onShowMaterial() {
        const quill = new Quill('#quill-container', { theme: 'snow' });
        this.quill = quill;
        console.log("hello")
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

                <br></br>
                <br></br>
                <Button style={{ margin: 'auto', display: 'block' }} onClick={e => this.setState({ materialCreate: true })}>Upload Study Material</Button>
                <br></br>
                <br></br>
                <br></br>

                <h3>Your feed</h3>
                <br></br>
                <br></br>
                <br></br>

                <Row>
                    <Col sm="12">
                        <Card body>
                            <Card.Title>Signal and the Noise</Card.Title>
                            <br></br>
                            <Card.Text>2019CS001</Card.Text>
                            <Card.Text><small>The Signal and the Noise: Why Most Predictions Fail – but Some Don’t
                                (alternatively stylized as The Signal and the Noise : Why So Many Predictions Fail – but Some Don’t)
                                is a 2012 book by Nate Silver detailing the art of using probability and statistics as applied to real-world circumstances.
                                The book includes case studies from baseball, elections, climate change, the 2008 financial crash, poker, and weather forecasting.
                                Published in the United States on September 27, 2012,
                                The Signal and The Noise reached the New York Times Best Sellers list as No. 12 for non-fiction hardback
                                books after its first week in print. </small></Card.Text>
                            <Button style={{ float: 'right', }}>Download Material</Button>
                        </Card>
                    </Col>
                </Row>
                <br></br>
                <br></br>
                <Row>
                    <Col sm="12">
                        <Card body>
                            <Card.Title>Big Data is Huge Data</Card.Title>
                            <br></br>
                            <Card.Text>2019CS002</Card.Text>
                            <Card.Text><small>The Signal and the Noise: Why Most Predictions Fail – but Some Don’t
                                (alternatively stylized as The Signal and the Noise : Why So Many Predictions Fail – but Some Don’t)
                                is a 2012 book by Nate Silver detailing the art of using probability and statistics as applied to real-world circumstances.
                                The book includes case studies from baseball, elections, climate change, the 2008 financial crash, poker, and weather forecasting.
                                Published in the United States on September 27, 2012,
                                The Signal and The Noise reached the New York Times Best Sellers list as No. 12 for non-fiction hardback
                                books after its first week in print. </small></Card.Text>
                            <Button style={{ float: 'right', }}>Download Material</Button>
                        </Card>
                    </Col>
                </Row>





                <Modal
                    show={this.state.materialCreate}
                    size="lg"
                    centered
                    onHide={e => { this.setState({ materialCreate: false }) }}
                    onShow={this.onShowMaterial}
                >
                    <Modal.Header closeButton>
                        <Modal.Title id="contained-modal-title-vcenter">
                            Upload Study Material
                        </Modal.Title>
                    </Modal.Header>
                    <Modal.Body>
                        <Form>
                            <Form.Control size="lg" type="text" placeholder="Enter Title" />
                            <br />
                            <Form.Control size="lg" type="text" placeholder="Enter Course ID" />
                            <br></br>
                            <h6>Description</h6>
                            <div id="quill-container">
                            </div>
                            <br></br>
                            <h6>Upload Material</h6>
                            <br></br>
                            <FilePond
                                server = "http://127.0.0.1:5002/submit"
                                allowMultiple={true}
                                onupdatefiles={(fileItems) => { this.setState({ files: fileItems.map(fileItem => fileItem.file) }); }}
                            />
                            <br></br>
                            <center>
                                <Button onClick={e => { console.log(this.state) }}>Upload</Button>
                            </center>
                        </Form>

                    </Modal.Body>
                    <Modal.Footer>
                        <Button onClick={e => { console.log(this.quill.getContents) }}>Post</Button>
                    </Modal.Footer>
                </Modal>



            </>
        );
    }
}






export default Material;