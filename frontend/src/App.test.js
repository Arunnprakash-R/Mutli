import { render, screen } from '@testing-library/react';
import App from './App';

test('renders welcome translator heading', () => {
  render(<App />);
  const headingElement = screen.getByText(/Welcome Translator/i);
  expect(headingElement).toBeInTheDocument();
});
