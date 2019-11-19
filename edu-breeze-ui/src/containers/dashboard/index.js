import React, { Component } from 'react';
import { connect } from 'react-redux';
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import Navbar from 'react-bootstrap/Navbar';
import Nav from 'react-bootstrap/Nav';
import Jumbotron from 'react-bootstrap/Jumbotron';
import Card from 'react-bootstrap/Card';
import Button from 'react-bootstrap/Button';
import { push } from 'connected-react-router';
import { userActions } from './../../store/actions/userActions.js';
import reactIcon from './../../resources/favicon.ico';
import icon from './../../resources/favicon.ico';
import './dashboard.css';

class Dashboard extends Component {
    constructor(props) {
        super(props);

        this.state = {
            isPageLoading: true,
        };
    }

    componentDidMount() {
        console.log('dashboardMounted', this.props);
        if (!this.props.loggedIn && !this.props.token) {
            console.log('DidMount:Not LoggedIn');
            this.props.flowRoute('/login');
        }

        // User data does not exist
        if (!this.props.user) {
            this.props.getUserAction(this.props.token, (resp, error) => {
                if (error) {
                    if (error.response.status === 404) {
                        // Expired or logged out relogin
                        this.props.flowRoute('/login');
                    }
                } else {
                    this.setState({
                        ...this.state,
                        isPageLoading: false,
                    });
                }
            });
        }
    }

    userSpecific() {
        return (
            <>
                <Jumbotron fluid>
                    <Container>
                        <h1>Hi {this.props.user.name.split(' ')[0]}!</h1>
                        <p>
                            Welcome to EduBreeze
                        </p>
                    </Container>
                </Jumbotron>

                <Container>
                    <Row>
                        <Col xs={12} md={4}>
                            <Card style={{ width: '18rem' }}>
                                <Card.Img variant="top" src={reactIcon} />
                                <Card.Body>
                                    <Card.Title>Courses</Card.Title>
                                    <Button variant="primary" className="btn-round">></Button>
                                </Card.Body>
                            </Card>
                        </Col>
                        <Col xs={12} md={4}>
                            <Card style={{ width: '18rem' }}>
                                <Card.Img variant="top" src={reactIcon} />
                                <Card.Body>
                                    <Card.Title>Courses</Card.Title>
                                    <Button variant="primary" className="btn-round">></Button>
                                </Card.Body>
                            </Card>
                        </Col>
                        <Col xs={12} md={4}>
                            <Card style={{ width: '18rem' }}>
                                <Card.Img variant="top" src={reactIcon} />
                                <Card.Body>
                                    <Card.Title>Courses</Card.Title>
                                    <Button variant="primary" className="btn-round">></Button>
                                </Card.Body>
                            </Card>
                        </Col>
                        <Col xs={12} md={4}>
                            <Card style={{ width: '18rem' }}>
                                <Card.Img variant="top" src={reactIcon} />
                                <Card.Body>
                                    <Card.Title>Courses</Card.Title>
                                    <Button variant="primary" className="btn-round">></Button>
                                </Card.Body>
                            </Card>
                        </Col>
                    </Row>
                </Container>
            </>
        )
    }

    render() {
        return (
            <>
                <Navbar expand="lg" bg="dark" variant="dark">
                    <Navbar.Brand href="#home">
                        <img
                            alt=""
                            src={icon}
                            width="30"
                            height="30"
                            className="d-inline-block align-top"
                        />
                        EduBreeze
                </Navbar.Brand>
                    <Navbar.Toggle aria-controls="responsive-navbar-nav" />
                    <Navbar.Collapse id="responsive-navbar-nav">
                        <Nav.Link href="#features">Features</Nav.Link>
                        <Nav.Link href="#pricing">Logout</Nav.Link>
                    </Navbar.Collapse>
                </Navbar>

                {this.state.isPageLoading ? null : this.userSpecific()}

            </>
        );
    }
};

function mapStateToProps(state) {
    console.log(state);

    const {
        loggedIn,
        token,
        user,
    } = state.authentication;

    return {
        loggedIn,
        token,
        user,
    };
}

const mapActionsToProps = {
    ...userActions,
    flowRoute: path => push(path),
};

export default connect(
    mapStateToProps,
    mapActionsToProps,
)(Dashboard);