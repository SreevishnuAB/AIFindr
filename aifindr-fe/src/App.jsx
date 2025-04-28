import { useState, useEffect } from 'react'
import Header from './components/Header'
import './App.css'
import Home from './components/Home'
import ErrorBox from './components/ErrorBox'
import Profile from './components/Profile'

function App() {
  const [id, setId] = useState(null)
  const [name, setName] = useState(null)
  const [profileText, setProfileText] = useState(null)
  const [errorMessage, setErrorMessage] = useState(null)
  const [profile, setProfile] = useState(null)

  useEffect(() => {
    console.log("Retrieving profile from session storage");
    
    if (sessionStorage.getItem("profile") !== null){
      const profile = JSON.parse(sessionStorage.getItem("profile"));
      console.log("Profile found in session storage: ", profile);
      setProfile(profile);
      setId(profile.id);
    }
  }, []); 

  function updateNameInput(name){
    setName(name);
  }

  function updateProfile(profile){
    setProfile(profile);
  }

  function updateProfileTextInput(profileText){
    setProfileText(profileText);
  }

  function openErrorBox(errorMessage){
    setErrorMessage(errorMessage)
    setTimeout(() => {
      setErrorMessage(null)
    }, 3000);
  }


  async function submitProfile(){
    if (!name || !profileText){
      openErrorBox("Please fill in all fields")
      return;
    }
    const backend_url = import.meta.env.VITE_BACKEND_URL || "http://localhost:8000";
    console.log(backend_url);
    
    try{
      // console.log("Submitting profile with name: ", name, " and profileText: ", profileText)
      const res = await fetch(`${backend_url}/aifindr/api/v1/profiles`, {
        method: "POST",
        body: JSON.stringify({"name": name, "profileText": profileText}),
        headers: {
          'Accept': 'application/json',
          'Content-Type': 'application/json'
        },
      });
      if (res.status === 200) {
        const data = await res.json();
        console.log("Profile submitted successfully: ", data);
        setProfile(data);
        sessionStorage.setItem("profile", JSON.stringify(data));
        console.log("stored profile in session storage");
        setId(data.id);
      }
      else{
        console.error("Error: ", res.json());
      }

    }
    catch(err){
      console.error(err)
      openErrorBox("Error submitting your profile. Please try again.")
    }
  }


  return (
    <>
    <Header/>
    {errorMessage && <ErrorBox errorMessage={errorMessage}/>}
    <div id="root">
    {id?<Profile profile={profile} handleProfileUpdate={updateProfile} handleError={openErrorBox} />:<Home handleNameInput={updateNameInput} handleProfileTextInput={updateProfileTextInput} handleGo={submitProfile}/>}
    </div>
    </>
  )
}

export default App;
