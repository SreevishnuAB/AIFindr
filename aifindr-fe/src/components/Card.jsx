import "./Card.css";
import { useState } from "react";

function Card({ profile, score, query, onError }) {
    const [reason, setReason] = useState(null);
    const [showReason, setShowReason] = useState(false);

    async function onExplain(){
        if (reason){
            setShowReason(!showReason);
            return;
        }
        const backend_url = import.meta.env.VITE_BACKEND_URL || "http://localhost:8000";
        try{
            const res = await fetch(`${backend_url}/aifindr/api/v1/explain`, {
                method: "POST",
                body: JSON.stringify({"query": query, "profileText": profile.profileText}),
                headers: {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json'
                },
            });
            if (res.status === 200) {
                const data = await res.json();
                console.log(data);
                
                setReason(data.reason);
                setShowReason(true);
            }
        }
        catch(error) {
            console.error("Error fetching explanation: ", error);
            onError(error);
        }
    }

    function handleBack(){
        setShowReason(false);
    }
    
    return (
        <div className="card">
            <div className="card-header">
                <h2>{profile.name}</h2>
                <div className="score">{Math.round(score)}%</div>
            </div>
            <br className="br"/>
            <div className="card-body">
                {!showReason?profile.profileText:reason}
            </div>
            <br className="br"/>
            {!showReason?<button onClick={()=>onExplain()}>Why?</button>:<button className="btn-inverse" onClick={()=>handleBack()}>Back</button>}
        </div>
    );
}

export default Card;