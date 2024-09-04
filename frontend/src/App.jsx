import { Container } from "react-bootstrap";
import Header from "./components/Header";
import Footer from "./components/Footer";
import { Outlet } from "react-router-dom";

const App = () => {
	return (
		<div className="app">
			<Header />
			<main className="main py-4">
				<Container>
					<Outlet />
				</Container>
			</main>
			<Footer />
		</div>
	);
};

export default App;
