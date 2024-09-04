import { Navbar, Nav, Container } from "react-bootstrap";
import { FaEye, FaUser, FaPumpSoap } from "react-icons/fa";

const Header = () => {
	return (
		<header className="header">
			<Navbar bg="dark" expand="md" variant="dark" collapseOnSelect>
				<Container>
					<Navbar.Brand href="/">
						<FaPumpSoap className="navbar-logo" /> FragrancePriceFinder
					</Navbar.Brand>
					<Navbar.Toggle aria-controls="basic-navbar-nav" />
					<Navbar.Collapse id="basic-navbar-nav">
						<Nav className="ms-auto">
							<Nav.Link href="/watch">
								<FaEye /> Watch List
							</Nav.Link>
							<Nav.Link href="/login">
								<FaUser /> Sign In
							</Nav.Link>
						</Nav>
					</Navbar.Collapse>
				</Container>
			</Navbar>
		</header>
	);
};

export default Header;
