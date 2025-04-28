import "./Profile.css";
import { useState } from "react";
import Card from "./Card";


function Profile({ profile, handleProfileUpdate, handleError}){

    const backend_url = import.meta.env.VITE_BACKEND_URL || "http://localhost:8000";

    const [editMode, setEditMode] = useState(false);
    const [profileText, setProfileText] = useState(profile.profileText);
    const [results, setResults] = useState([]);
    const [query, setQuery] = useState(null);

    async function onUpdate(){
        try{
            const res = await fetch(`${backend_url}/aifindr/api/v1/profiles/${profile.id}`, {
                method: "PATCH",
                body: JSON.stringify({"name": profile.name, "profileText": profileText}),
                headers: {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json'
                },
            });

            if (res.status !== 200) {
                const data = await res.json();

                handleError(`Error: ${data}`);
                return;
            }
        }
        catch(error) {
            handleError(`Error: ${error}`);
        }
        const updatedProfile = {
            ...profile,
            profileText: profileText
        };
        handleProfileUpdate(updatedProfile);
        setEditMode(false);
    }

    async function onSearch(){
        const res = await fetch(`${backend_url}/aifindr/api/v1/search`, {
            method: "POST",
            body: JSON.stringify({"query": query}),
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
        });

        if (res.status === 200) {
            const data = await res.json();

            const filtered_results = data.results.filter((result) => result.profile.id !== profile.id);
            console.log(filtered_results);
            if (filtered_results.length === 0){
                handleError("No matching results found");
                return;
            }
            setResults(filtered_results);
        }
        else{
            const data = await res.json();
            handleError(`Error: ${data}`);
        }
    }

    return (
        <div className="search-body">
            <div className="search-header">
                <h2>{profile.name}'s Profile</h2>
            {!editMode ?
            <><div className="profile-text">{profile.profileText}</div><button onClick={()=>setEditMode(true)}>Edit</button></>
            :<><textarea defaultValue={profileText} className="profile-text profile-input" onChange={(e) => setProfileText(e.target.value)}/><button onClick={async ()=> await onUpdate()}>Update</button></>}
            </div>
            <div className="controls">
                <input className="query" type="text" placeholder="What are you looking for?" onChange={(e)=>setQuery(e.target.value)}/>
                <button className="search-button" onClick={() => onSearch()}>Search</button>
            </div>
            <div className="search-results">
                {results.map((result, index) => <Card key={index} profile={result.profile} score={result.score} query={query} onError={handleError}/>)}
            </div>
        </div>
    );
}

export default Profile;