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
import './blog.css';
import { Component } from 'react';
import { connect } from 'react-redux';
import Container from 'react-bootstrap/Container';


class Blog extends Component {
    constructor(props) {
        super(props);

        this.state = {
            modalOpen: false,
            isPageLoading: true,
            files: [],
            blogCreate: false,
            blogRead: false,
        };

        this.onShowBlog = this.onShowBlog.bind(this);
    }

    onShowBlog() {
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
                <Button style={{ margin: 'auto', display: 'block' }} onClick={e => this.setState({ blogCreate: true })}>Create Post</Button>
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
                            <Card.Text>John Doe</Card.Text>
                            <Card.Text><small>The Signal and the Noise: Why Most Predictions Fail – but Some Don’t
                                (alternatively stylized as The Signal and the Noise : Why So Many Predictions Fail – but Some Don’t)
                                is a 2012 book by Nate Silver detailing the art of using probability and statistics as applied to real-world circumstances.
                                The book includes case studies from baseball, elections, climate change, the 2008 financial crash, poker, and weather forecasting.
                                Published in the United States on September 27, 2012,
                                The Signal and The Noise reached the New York Times Best Sellers list as No. 12 for non-fiction hardback
                                books after its first week in print. It dropped to No. 20 in the second week, before rising to No. 13 in the third,
                                and remaining on the non-fiction hardback top 15 list for the following thirteen weeks, with a highest weekly ranking of
                                No. 4. The book’s already strong sales soared right after election night, November 6, jumping 800% and becoming the
                                second best seller on Amazon.com.[2] The Signal and the Noise (print edition) was named Amazon’s No. 1 Best
                                NonFiction Book for 2012. It was named by the Wall Street Journal as one of the ten best books of nonfiction
                                published in 2012. </small></Card.Text>
                            <Button style={{ float: 'right', }} onClick={e => this.setState({ blogRead: true })}>Read More</Button>
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
                            <Card.Text>Sarah Appleseed</Card.Text>
                            <Card.Text><small>The Signal and the Noise: Why Most Predictions Fail – but Some Don’t
                                (alternatively stylized as The Signal and the Noise : Why So Many Predictions Fail – but Some Don’t)
                                is a 2012 book by Nate Silver detailing the art of using probability and statistics as applied to real-world circumstances.
                                The book includes case studies from baseball, elections, climate change, the 2008 financial crash, poker, and weather forecasting.
                                Published in the United States on September 27, 2012,
                                The Signal and The Noise reached the New York Times Best Sellers list as No. 12 for non-fiction hardback
                                books after its first week in print. It dropped to No. 20 in the second week, before rising to No. 13 in the third,
                                and remaining on the non-fiction hardback top 15 list for the following thirteen weeks, with a highest weekly ranking of
                                No. 4. The book’s already strong sales soared right after election night, November 6, jumping 800% and becoming the
                                second best seller on Amazon.com.[2] The Signal and the Noise (print edition) was named Amazon’s No. 1 Best
                                NonFiction Book for 2012. It was named by the Wall Street Journal as one of the ten best books of nonfiction
                                published in 2012. </small></Card.Text>
                            <Button style={{ float: 'right', }} onClick={e => this.setState({ blogRead: true })}>Read More</Button>
                        </Card>
                    </Col>
                </Row>
                <br></br>
                <br></br>
                <Row>
                    <Col sm="12">
                        <Card body>
                            <Card.Title>Human Firewall</Card.Title>
                            <br></br>
                            <Card.Text>Doe John</Card.Text>
                            <Card.Text><small>The Signal and the Noise: Why Most Predictions Fail – but Some Don’t
                                (alternatively stylized as The Signal and the Noise : Why So Many Predictions Fail – but Some Don’t)
                                is a 2012 book by Nate Silver detailing the art of using probability and statistics as applied to real-world circumstances.
                                The book includes case studies from baseball, elections, climate change, the 2008 financial crash, poker, and weather forecasting.
                                Published in the United States on September 27, 2012,
                                The Signal and The Noise reached the New York Times Best Sellers list as No. 12 for non-fiction hardback
                                books after its first week in print. It dropped to No. 20 in the second week, before rising to No. 13 in the third,
                                and remaining on the non-fiction hardback top 15 list for the following thirteen weeks, with a highest weekly ranking of
                                No. 4. The book’s already strong sales soared right after election night, November 6, jumping 800% and becoming the
                                second best seller on Amazon.com.[2] The Signal and the Noise (print edition) was named Amazon’s No. 1 Best
                                NonFiction Book for 2012. It was named by the Wall Street Journal as one of the ten best books of nonfiction
                                published in 2012. </small></Card.Text>
                            <Button style={{ float: 'right', }} onClick={e => this.setState({ blogRead: true })}>Read More</Button>
                        </Card>
                    </Col>

                </Row>






                <Modal
                    show={this.state.blogCreate}
                    size="lg"
                    centered
                    onHide={e => { this.setState({ blogCreate: false }) }}
                    onShow={this.onShowBlog}
                >
                    <Modal.Header closeButton>
                        <Modal.Title id="contained-modal-title-vcenter">
                            Create a blog post
        </Modal.Title>
                    </Modal.Header>
                    <Modal.Body>
                        <Form>
                            <Form.Control size="lg" type="text" placeholder="Enter Title" />
                            <br />
                            <DropdownButton id="dropdown-basic-button" title="Semester">
                                <Dropdown.Item href="#/action-1">Semester 7</Dropdown.Item>
                                <Dropdown.Item href="#/action-2">Semester 5</Dropdown.Item>
                                <Dropdown.Item href="#/action-3">Semester 3</Dropdown.Item>
                            </DropdownButton>
                            <br></br>
                            <Form.Control type="text" placeholder="Enter three keywords" />
                            <br />
                            <h6>Description</h6>
                            <div id="quill-container">
                            </div>
                        </Form>

                    </Modal.Body>
                    <Modal.Footer>
                        <Button onClick={e => { console.log(this.quill.getContents) }}>Post</Button>
                    </Modal.Footer>
                </Modal>



                <Modal
                    show={this.state.blogRead}
                    size="lg"
                    centered
                    onHide={e => { this.setState({ blogRead: false }) }}
                    onShow={this.onShowBlog}
                >
                    <Modal.Header closeButton>
                        <Modal.Title id="contained-modal-title-vcenter">
                            Blog Article
        </Modal.Title>
                    </Modal.Header>
                    <Modal.Body>
                        <h4>Signal and the Noise</h4>
                        <p><small>The Signal and the Noise: Why Most Predictions Fail – but Some Don’t
                                    (alternatively stylized as The Signal and the Noise : Why So Many Predictions Fail – but Some Don’t)
                                    is a 2012 book by Nate Silver detailing the art of using probability and statistics as applied to real-world circumstances.
                                    The book includes case studies from baseball, elections, climate change, the 2008 financial crash, poker, and weather forecasting.
                                    Published in the United States on September 27, 2012,
                                    The Signal and The Noise reached the New York Times Best Sellers list as No. 12 for non-fiction hardback
                                    books after its first week in print. It dropped to No. 20 in the second week, before rising to No. 13 in the third,
                                    and remaining on the non-fiction hardback top 15 list for the following thirteen weeks, with a highest weekly ranking of
                                    No. 4. The book’s already strong sales soared right after election night, November 6, jumping 800% and becoming the
                                    second best seller on Amazon.com.[2] The Signal and the Noise (print edition) was named Amazon’s No. 1 Best
                                    NonFiction Book for 2012. It was named by the Wall Street Journal as one of the ten best books of nonfiction
                                    published in 2012. The book was first released in the United Kingdom in April 2013, with the title The Signal and the
                                    Noise: The Art and Science of Prediction, in hardback under an Allen Lane imprint [5] and in paperback under a Penguin imprint.
                                    It was published in Brazil in a Portuguese translation, O sinal e o ruído, in June 2013.[7] A German edition was released in September 2013
                                    by the publisher Heine Verlag, using a somewhat different main title: The Calculation of the Future.[8] An Italian version,
                                    Il segnale e il rumore. Arte e scienza della previsione, appeared in October 2013. A Finnish translation (Sinaali ja Kohina)
                                    appeared in 2014. The book was published in simplified Chinese characters by China Citic Press in Beijing[10] as well as in traditional
                                    Chinese characters by Suncolor Press in Taipei in Fall 2013. It was published in Japanese in November 2013.[12]
                                    A Spanish translation appeared in April 2014, under the title La señal y el ruido. In 2013, an edition was published in
                                    Romanian by Publica press: Semnalul și zgomotul: de ce atât de multe predicții dau greș - pe când altele reușesc. In May 2014,
                                    an edition was published in Czech: Signál a šum. Většina předpovědí selže. Některé ne. A Polish edition was scheduled for publication
                                    in hardcover in 2015 by Helion: Sygnal I szum: Sztuka prognozowania w erze technologii. The Signal and the Noise was first published in paperback
                                    in the United States on February 3, 2015.[17] It contained a new introduction.[18] It reached The New York Times paperback best seller list, ranked
                                    No. 4 in the field of Education in March 2015.
                                </small></p>

                    </Modal.Body>
                    <Modal.Footer>

                    </Modal.Footer>
                </Modal>

            </>
        );
    }
}






export default Blog;



