import "./ErrorBox.css";

function ErrorBox({ errorMessage }) {
  return (
    <div className="error-box">
      {errorMessage}
    </div>
  );
}

export default ErrorBox;