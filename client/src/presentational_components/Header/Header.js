import React from "react";
import "./header.css";

import { Navbar, Nav } from "react-bootstrap";
import { Link } from "react-scroll";
class Header extends React.Component {
  render() {
    return (
      <div className="navbar-container">
        <Navbar collapseOnSelect expand="lg">
          <Navbar.Brand className="brand" href="#home">
            BRSV
          </Navbar.Brand>
          <Navbar.Toggle aria-controls="responsive-navbar-nav" />
          <Navbar.Collapse id="responsive-navbar-nav">
            <Nav className="ml-auto">
              <Link
                activeClass="active"
                to="upload"
                spy={true}
                smooth={true}
                offset={250}
                duration={700}
              >
                <Nav.Link className="link" href="">
                  Uploads
                </Nav.Link>
              </Link>
              <Link
                  activeClass="active"
                  to="result"
                  spy={true}
                  smooth={true}
                  offset={250}
                  duration={700}
              >
              <Nav.Link className="link" href="#features">
                Results
              </Nav.Link>
              </Link>
              {/*TODO LOGIN AND SIGNUP*/}
              {/*<Nav.Link className="link" href="#features">*/}
              {/*  Login/SignUp*/}
              {/*</Nav.Link>*/}
            </Nav>
          </Navbar.Collapse>
        </Navbar>
      </div>
    );
  }
}

export default React.memo(Header);
