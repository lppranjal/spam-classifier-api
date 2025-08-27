# 📧 Spam-Classifier API + Angular UI

Live demo → **[https://spam-classifier-api-vrk2.onrender.com](https://spam-classifier-api-vrk2.onrender.com)**  

![](assets/ui.png)  
*Landing page – paste text and hit “Classify”*

![](assets/ui-spam.png)  
*Example result (“Spam” detected)*

![](assets/ui-ham.png)  
*Example result (Ham)*

---

## 🛠 Tech Stack
- **FastAPI** – REST endpoint `/predict`
- **scikit-learn** – TF-IDF + model saved as `model.joblib`
- **Angular 17 (stand-alone)** – single-page UI
- **Render** – one service hosts API & static files
