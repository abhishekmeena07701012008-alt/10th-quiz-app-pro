// Network Checker Logic for 10th Quiz Pro
function checkNetworkStatus() {
    const body = document.body;

    if (!navigator.onLine) {
        // अगर इंटरनेट बंद है, तो स्क्रीन पर मैसेज दिखाएं
        showNoInternetUI();
    } else {
        // अगर इंटरनेट चालू है, तो एरर मैसेज हटाएं और ऐप लोड करें
        removeNoInternetUI();
    }
}

function showNoInternetUI() {
    // अगर पहले से ही एरर मैसेज मौजूद है तो दोबारा न बनाएं
    if (document.getElementById('network-error-overlay')) return;

    const overlay = document.createElement('div');
    overlay.id = 'network-error-overlay';
    overlay.style = `
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-color: #ffffff;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        z-index: 9999;
        font-family: Arial, sans-serif;
        text-align: center;
        padding: 20px;
    `;

    overlay.innerHTML = `
        <div style="font-size: 50px; margin-bottom: 20px;">📶❌</div>
        <h2 style="color: #d32f2f;">नेटवर्क चालू नहीं है</h2>
        <p style="color: #555; font-size: 18px;">
            अरे! 10th प्रो ऐप लोड करने के लिए इंटरनेट की आवश्यकता है। <br>
            कृपया अपना मोबाइल डेटा या वाई-फाई चालू करें।
        </p>
        <button onclick="window.location.reload()" style="
            margin-top: 20px;
            padding: 10px 25px;
            background-color: #1a73e8;
            color: white;
            border: none;
            border-radius: 5px;
            font-size: 16px;
            cursor: pointer;">
            फिर से कोशिश करें
        </button>
    `;

    document.body.appendChild(overlay);
}

function removeNoInternetUI() {
    const overlay = document.getElementById('network-error-overlay');
    if (overlay) {
        overlay.remove();
    }
}

// घटना की निगरानी करें (अगर चलते-चलते नेट बंद हो जाए)
window.addEventListener('offline', showNoInternetUI);
window.addEventListener('online', removeNoInternetUI);

// ऐप शुरू होते ही चेक करें
checkNetworkStatus();
