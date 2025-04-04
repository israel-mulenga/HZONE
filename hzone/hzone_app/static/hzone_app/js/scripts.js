
    //AFFECTATIONS DES VARIABLES
    const formPublication = document.getElementById("formPublication"); //formulaire qui s'adapte pour poster un bien en location ou en vente
    const options = document.getElementById("options"); // options vendre ou louer
    const optionLocation = document.getElementById("optionLocation");
    const divOptionLocation = document.getElementById("divOptionLocation");
    const likeButton = document.getElementById("likeButton");
    const likeButtonIcon = document.getElementById("likeButtonIcon")
    const whatsappShare = document.getElementById("whatsapp-share");
    const copyButton = document.getElementById("copyButton");
    const messageCopyButton = document.getElementById("messageCopyButton");

    


    //DEFINITION DES FONCTIONS
    const likeOrUnlike = ()=>{
      likeButtonIcon.addEventListener('click', function(){
        let isLiked = likeButton.classList.contains("not-liked");
        if(isLiked){
        likeButton.classList.remove("not-liked");
        likeButton.classList.add('liked');
        likeButtonIcon.classList.remove("far", 'text-black');
        likeButtonIcon.classList.add("fas", "text-danger");
      }else{
        likeButton.classList.remove('liked');
        likeButton.classList.add("not-liked");
        likeButtonIcon.classList.remove("fas", "text-danger");
        likeButtonIcon.classList.add("far", 'text-black');
      }
      })
    }

    //partager sur whatsapp
    const  shareLink = () => {
      whatsappShare.addEventListener('click', function() {
      const url = window.location.href; // URL actuelle de la page 
      const text = "Venez visiter Hzone et Trouver l'habitation de vos rêves: "; 
      const message = `${text}${url}`; 
      const whatsappURL = `https://wa.me/?text=${encodeURIComponent(message)}`;
      window.open(whatsappURL, '_blank'); });
    }

    const copyLink = () => {
      const displayMessage = (message) => {
        $("#messageCopyButton").addClass("animate__animated animate__fadeInUp");
        messageCopyButton.textContent = message;
        // Effacer le message après 3 secondes
        setTimeout(() => {
          $("#messageCopyButton").removeClass("animate__animated animate__fadeInUp");
          messageCopyButton.textContent = ""
        }, 3000);
      };
    
      copyButton.addEventListener('click', function() {
        const url = window.location.href;
        navigator.clipboard.writeText(url).then(() => {
          displayMessage("Lien copié!");
        }).catch(err => {
          console.error("Echec de la copie: ", err);
          displayMessage("Echec de la copie.");
        });
      });
    };
    

    
    // formulaire pour un bien en vente
    const formVente = () => {
      formPublication.innerHTML =`<div class="container mt-5"> 
            <h2>Formulaire de Mise en Vente</h2> 
            <form> 
              <!-- Adresse --> 
              <div class="mb-3"> 
                <label for="address" class="form-label">Adresse</label>
                <input type="text" class="form-control" id="address" placeholder="Entrez l'adresse complète" required>
              </div>
              <!-- Prix -->
              <div class="mb-3">
                <label for="price" class="form-label">Prix</label>
                <input type="number" class="form-control" id="price" placeholder="Entrez le prix demandé en dollars" required>
              </div>
              <!-- Type de Propriété -->
              <div class="mb-3">
                <label for="propertyType" class="form-label">Type de Propriété</label>
                <select class="form-select" id="propertyType" required>
                  <option value="">Choisissez...</option>
                  <option value="maison_individuelle">Maison Individuelle</option>
                  <option value="appartement">Appartement</option>
                  <option value="duplex">Duplex</option>
                  <option value="chambre">Chambre</option>
                  <option value="autre">autre</option>
                </select>
              </div>
              <!-- Superficie -->
              <div class="mb-3">
                <label for="superficie" class="form-label">Superficie (en m²)</label>
                <input type="number" class="form-control" id="superficie" placeholder="Entrez la superficie" required>
              </div>
              <!-- Nombre de Chambres -->
               <div class="mb-3">
                <label for="chambres" class="form-label">Nombre de Chambres</label>
                <input type="number" class="form-control" id="chambres" placeholder="Entrez le nombre de chambres" required>
              </div>
              <!-- Nombre de Salles de Bain -->
               <div class="mb-3">
                <label for="sallesBain" class="form-label">Nombre de Salles de Bain</label>
                <input type="number" class="form-control" id="sallesBain" placeholder="Entrez le nombre de salles de bain" required>
              </div>
              <!-- Agencement -->
              <div class="mb-3">
                <label for="agencement" class="form-label">Agencement</label>
                <textarea class="form-control" id="agencement" rows="3" placeholder="Décrivez l'agencement des pièces" required></textarea>
              </div> <!-- Espaces Extérieurs --> <div class="mb-3"> <label for="espacesExt" class="form-label">Espaces Extérieurs</label>
                <textarea class="form-control" id="espacesExt" rows="3" placeholder="Décrivez les espaces extérieurs (jardin, terrasse, etc.)" required></textarea>
              </div>
              <!-- Quartier -->
              <div class="mb-3">
                <label for="quartier" class="form-label">Quartier</label>
                <input type="text" class="form-control" id="quartier" placeholder="Donnez uniquement le nom du quartier" required>
              </div>
              <!-- Photos -->
              <div class="mb-3">
                <label for="photos" class="form-label">Photos</label>
                <input type="file" class="form-control" id="photos" multiple required>
              </div>
              <!-- Numéro propriétaire --> 
              <div class="mb-3"> 
                <label for="address" class="form-label">Numéro de téléphone</label>
                <input type="tel" class="form-control" id="numTelPro" placeholder="Entre le numéro de téléphone sur lequel vous receverez le virement" required>
              </div>
              <!-- Bouton de Soumission -->
               <button type="submit" class="btn btn-primary">Soumettre</button>
              </form>
            </div>`;
    }


    // formulaire pour la location d'une chambre
    const locationChambre = ()=>{
      formPublication.innerHTML = `
  <div class="container mt-5">
    <h2>Formulaire de Location de Chambre d'Hôtel</h2>
    <form>
      <!-- Nom de l'Hôtel -->
      <div class="mb-3">
        <label for="hotelName" class="form-label">Nom de l'Hôtel</label>
        <input type="text" class="form-control" id="hotelName" placeholder="Entrez le nom de l'hôtel" required>
      </div>
      
      <!-- Adresse -->
      <div class="mb-3">
        <label for="address" class="form-label">Adresse</label>
        <input type="text" class="form-control" id="address" placeholder="Entrez l'adresse complète" required>
      </div>
      
      <!-- Numéro de Téléphone -->
      <div class="mb-3">
        <label for="phone" class="form-label">Numéro de Téléphone</label>
        <input type="tel" class="form-control" id="phone" placeholder="Entrez le numéro de téléphone sur lequel doit s'effectuer le virement" required>
      </div>
      
      <!-- Prix par Nuit -->
      <div class="mb-3">
        <label for="price" class="form-label">Prix par Nuit</label>
        <input type="number" class="form-control" id="price" placeholder="Entrez le prix par nuit" required>
      </div>
      
      <!-- Type de Chambre -->
      <div class="mb-3">
        <label for="roomType" class="form-label">Type de Chambre</label>
        <select class="form-select" id="roomType" required>
          <option value="">Choisissez...</option>
          <option value="standard">Standard</option>
          <option value="deluxe">Deluxe</option>
          <option value="suite">Suite</option>
        </select>
      </div>
      
      <!-- Superficie -->
      <div class="mb-3">
        <label for="superficie" class="form-label">Superficie (en m²)</label>
        <input type="number" class="form-control" id="superficie" placeholder="Entrez la superficie" required>
      </div>
      
      <!-- Nombre de Lits -->
      <div class="mb-3">
        <label for="beds" class="form-label">Nombre de Lits</label>
        <input type="number" class="form-control" id="beds" placeholder="Entrez le nombre de lits" required>
      </div>
      
      <!-- Capacité d'Accueil -->
      <div class="mb-3">
        <label for="capacity" class="form-label">Capacité d'Accueil</label>
        <input type="number" class="form-control" id="capacity" placeholder="Nombre maximal de personnes" required>
      </div>
      
      <!-- Photos -->
      <div class="mb-3">
        <label for="photos" class="form-label">Photos</label>
        <input type="file" class="form-control" id="photos" multiple required>
      </div>
      
      <!-- Bouton de Soumission -->
      <button type="submit" class="btn btn-primary">Soumettre</button>
    </form>
  </div>`
      
    }

    // fonction qui gère les formulaires de publications
    const showFormPublication = () =>{
      options.addEventListener("change", ()=>{
      divOptionLocation.style.display = 'none'
      formPublication.innerHTML = ``
      if(options.value==="vendre"){
        formVente()
        $(document).ready(function() { setTimeout(function() { $("#formPublication").addClass("animate__animated animate__fadeInUp"); }, 1);  }); //afficher le formulaire de vente
      }else if(options.value==="louer"){
        divOptionLocation.style.display = "block";
        $(document).ready(function() { setTimeout(function() { $("#optionLocation").addClass("animate__animated animate__fadeInUp"); }, 10);  }); //affiche le formulaire du bien de location
        optionLocation.addEventListener("change", ()=>{
          if(optionLocation.value==="chambre"){
          locationChambre();
          $(document).ready(function() { setTimeout(function() { $("#formPublication").addClass("animate__animated animate__fadeInUp"); }, 10);  }); //affiche la location de chambre
        }
        })
      }
    })
    }

   

   $(document).ready(function() {
      $("#searchButton").click(function() {
        const searchTerm = $("#searchInput").val();
        const filterOption = $("#filterSelect").val();

        // Logique pour filtrer les résultats
        console.log("Recherche:", searchTerm, "Filtre:", filterOption);

        // Affiche les résultats filtrés
        $("#resultContainer").html(`<p>Résultats pour: "${searchTerm}" avec le filtre: "${filterOption}"</p>`);
      });
    });

    showFormPublication()
    likeOrUnlike()
    shareLink()
    copyLink()