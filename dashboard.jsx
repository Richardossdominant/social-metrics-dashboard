// src/App.js
import React, { useEffect, useState } from 'react';
import axios from 'axios';
import './App.css';

const App = () => {
    const [tiktokMetrics, setTikTokMetrics] = useState({});
    const [instagramMetrics, setInstagramMetrics] = useState({});
    const [googleAdsMetrics, setGoogleAdsMetrics] = useState({});

    useEffect(() => {
        axios.get('http://localhost:5000/metrics/tiktok')
            .then(response => setTikTokMetrics(response.data))
            .catch(error => console.error('Error fetching TikTok metrics:', error));

        axios.get('http://localhost:5000/metrics/instagram')
            .then(response => setInstagramMetrics(response.data))
            .catch(error => console.error('Error fetching Instagram metrics:', error));

        axios.get('http://localhost:5000/metrics/google_ads')
            .then(response => setGoogleAdsMetrics(response.data))
            .catch(error => console.error('Error fetching Google Ads metrics:', error));
    }, []);

    return (
        <div className="App">
            <h1>Social Media Metrics Dashboard</h1>
            <div className="metric-container">
                <h2>TikTok Metrics</h2>
                <pre>{JSON.stringify(tiktokMetrics, null, 2)}</pre>
            </div>
            <div className="metric-container">
                <h2>Instagram Metrics</h2>
                <pre>{JSON.stringify(instagramMetrics, null, 2)}</pre>
            </div>
            <div className="metric-container">
                <h2>Google Ads Metrics</h2>
                <pre>{JSON.stringify(googleAdsMetrics, null, 2)}</pre>
            </div>
        </div>
    );
};

export default App;
