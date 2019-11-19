import React, { Component } from 'react';
import { connect } from 'react-redux';
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import Form from 'react-bootstrap/Form';
import Button from 'react-bootstrap/Button';
import Alert from 'react-bootstrap/Alert';
import { push } from 'connected-react-router';
import { userActions } from './../../store/actions/userActions.js';
import './login.css';

import ebLogo from './../../resources/Logo.png';

class Login extends Component {
    constructor(props) {
        super(props);

        this.state = {
            username: '',
            password: '',
            submitted: false,
            isLoading: false,
            loginFailed: false,
            loginFailedMsg: "Incorrect Username or Password",
        };

        this.handleSubmit = this.handleSubmit.bind(this);
        this.handleChange = this.handleChange.bind(this);
    }

    handleSubmit(event) {
        console.log(this.state)
        event.preventDefault();

        const { submitted, ...userCreds } = this.state; // funny syntax

        console.log(userCreds);

        this.setState({
            ...this.state,
            isLoading: true,
        });

        this.props.loginAction(userCreds, (resp, error) => {
            if (error) {
                console.log(error, resp);
                this.setState({
                    ...this.state,
                    loginFailed: true,
                    loginFailedMsg: 'Oops! Something went wrong. Please try again',
                    isLoading: false,
                });
            } else {
                
                if(resp.login) {
                    console.log(resp);
                    this.props.proceedToDashboard('/dashboard');
                } else {
                    this.setState({
                        ...this.state,
                        loginFailed: true,
                        loginFailedMsg: resp.message,
                        isLoading: false,
                    });
                }
            }
        });
    }

    handleChange(event) {
        const { name, value } = event.target;

        this.setState({
            ...this.state,
            [name]: value,
        });
    }

    render() {
        return (
            <Container>
                <Row>
                    <Col></Col>
                    <Col xs={12} md={4}>
                        <div className="login-container justify-content-center">
                            <div className="justify-content-center">
                                <Row>
                                    <Col></Col>
                                    <Col>
                                        <img src={ebLogo} className="login-logo" alt="eb-logo" />
                                        <span className="logo-subtitle">
                                            One-stop Educational Institution Management
                                        </span>
                                    </Col>
                                    <Col></Col>
                                </Row>

                            </div>
                            <div className="form-container">
                                <Form onSubmit={this.handleSubmit}>
                                    <Form.Group controlId="formBasicEmail">
                                        <Form.Label>Username</Form.Label>
                                        <Form.Control
                                            name="username"
                                            type="text"
                                            placeholder="Enter username"
                                            onChange={this.handleChange}
                                            required
                                        />
                                        <Form.Text className="text-muted">
                                        </Form.Text>
                                    </Form.Group>

                                    <Form.Group controlId="formBasicPassword">
                                        <Form.Label>Password</Form.Label>
                                        <Form.Control
                                            name="password"
                                            type="password"
                                            placeholder="Password"
                                            onChange={this.handleChange}
                                            required
                                        />
                                    </Form.Group>

                                    <Button
                                        variant="primary"
                                        type="submit"
                                        className="submitButton"
                                        disabled={this.state.isLoading}
                                        block>
                                        {this.state.isLoading ? "Loading..." : "Login"}
                                    </Button>

                                    {this.state.loginFailed ?    
                                        <Alert variant="danger" size="lg" className="login-fail-alert">
                                            {this.state.loginFailedMsg}
                                        </Alert> : <></>
                                    }
                                </Form>
                            </div>
                        </div>
                    </Col>
                    <Col></Col>
                </Row>
            </Container>
        )
    }
}

const mapActionsToProps = {
    ...userActions,
    proceedToDashboard: (path) => push(path),
}

export default connect(
    null,
    mapActionsToProps,
)(Login)