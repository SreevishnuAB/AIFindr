import "./Home.css";

function Home({ handleNameInput, handleProfileTextInput, handleGo }){
    return (
        <div className="home">
            <input className="input" type="text" placeholder="What should we call you?" onChange={(e) => handleNameInput(e.target.value)} />
            <textarea className="input input-textarea" placeholder="Tell us a bit about yourself" onChange={(e)=>handleProfileTextInput(e.target.value)} />
            <button onClick={async () => await handleGo()}>Go</button>
        </div>
    );

}

export default Home;