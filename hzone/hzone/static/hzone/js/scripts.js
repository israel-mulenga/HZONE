const diapo = document.getElementById("diapo");
    
        // Les contenus de la diapositive
        const containDiapo1 = `
        <div class="slider-item" style="background-image: url(${window.staticImages.diapo1});">
            <div class="slider-content">
                <h1>TROUVER L'HABITATION DE VOS RÊVES</h1>
            </div>
        </div>`;
    
        const containDiapo2 = `
        <div class="slider-item" style="background-image: url(${window.staticImages.diapo2});">
            <div class="slider-content">
                <h1>METTEZ VOTRE BIEN EN LOCATION FACILEMENT</h1>
            </div>
        </div>`;
    
        const containDiapo3 = `
        <div class="slider-item" style="background-image: url(${window.staticImages.diapo3});">
            <div class="slider-content">
                <h1>VOTRE APPARTEMENT IDÉAL À PORTÉE DE MAIN</h1>
            </div>
        </div>`;
    
        // La fonction pour changer le contenu de la diapositive
        function changeContain(){
            if(diapo.innerHTML===containDiapo1){
                diapo.innerHTML = containDiapo2;
            }else if(diapo.innerHTML===containDiapo2){
                diapo.innerHTML = containDiapo3
            }else if(diapo.innerHTML===containDiapo3){
                diapo.innerHTML = containDiapo1
            }else{
                diapo.innerHTML = containDiapo1;
            }
        }
    
        $(document).ready(function() {
            changeContain();
            function animateDiapo(){
                setTimeout(function(){
                    $("#diapo").addClass("fade-out");
                }, 3000);
        
                setTimeout(function(){
                    $("#diapo").removeClass("fade-out").addClass("fade-in");
                }, 3700);
        
                setTimeout(function(){
                    changeContain();
                    $("#diapo").removeClass("fade-in");
                }, 3700);
        
                setTimeout(function(){
                    animateDiapo();
                }, 3900);
            }
            
            animateDiapo(); // L'appel de la fonction
        });