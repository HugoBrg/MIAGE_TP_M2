class MyLogo extends HTMLElement {
    html = `
    <p id="logo" class="tracking-in-contract-bck"></p>

    <p>Couleur: </p>
    <input type="color" id="colorSelect"> 

    <p>Bordure: </p>
    <input type="color" id="borderSelect"> 

    <p>Texte : </p>
    <input type="text" id="logoInputText" name="name" required minlength="3" maxlength="10" size="12">
    <button id="valider">Valider</button>
    
    <p>Taille : </p>
    <input type="range" min="5" max="150" value="12" id="slider">

    <br>
    <p>Style : </p>
    <select id="style">
        <option value="">--Please choose an option--</option>
        <option value="underline">Underline</option>
        <option value="overline">Overline</option>
        <option value="line-through">Line-through</option>
    </select>

    <p>Importer un modèle de comparaison : </p>
    <input type="text" id="logoImage" name="name" required minlength="1" maxlength="250" size="50">
    <button id="importer">Importer</button>
    <br>
    <br>
    <img id="image" src="https://cdn.iconscout.com/icon/free/png-256/coca-cola-1863554-1579762.png">
    `;
    
    style = `
    #logo {
    }

    .tracking-in-contract-bck {
        font-size: 50px;
        -webkit-animation: tracking-in-contract-bck 1s cubic-bezier(0.215, 0.610, 0.355, 1.000) both;
                animation: tracking-in-contract-bck 1s cubic-bezier(0.215, 0.610, 0.355, 1.000) both;
    }

   @-webkit-keyframes tracking-in-contract-bck {
     0% {
       letter-spacing: 1em;
       -webkit-transform: translateZ(400px);
               transform: translateZ(400px);
       opacity: 0;
     }
     40% {
       opacity: 0.6;
     }
     100% {
       -webkit-transform: translateZ(0);
               transform: translateZ(0);
       opacity: 1;
     }
   }
   @keyframes tracking-in-contract-bck {
     0% {
       letter-spacing: 1em;
       -webkit-transform: translateZ(400px);
               transform: translateZ(400px);
       opacity: 0;
     }
     40% {
       opacity: 0.6;
     }
     100% {
       -webkit-transform: translateZ(0);
               transform: translateZ(0);
       opacity: 1;
     }
   } 

    .text-focus-in {
        font-size: 50px;
        -webkit-animation: text-focus-in 1s cubic-bezier(0.550, 0.085, 0.680, 0.530) both;
                animation: text-focus-in 1s cubic-bezier(0.550, 0.085, 0.680, 0.530) both;
    }

    @-webkit-keyframes text-focus-in {
        0% {
            -webkit-filter: blur(12px);
                    filter: blur(12px);
            opacity: 0;
        }
        100% {
            -webkit-filter: blur(0px);
                    filter: blur(0px);
            opacity: 1;
        }
        }
        @keyframes text-focus-in {
        0% {
            -webkit-filter: blur(12px);
                    filter: blur(12px);
            opacity: 0;
        }
        100% {
            -webkit-filter: blur(0px);
                    filter: blur(0px);
            opacity: 1;
        }
    }

    .jello-horizontal {
        -webkit-animation: jello-horizontal 0.9s both;
                animation: jello-horizontal 0.9s both;
    }

    @-webkit-keyframes jello-horizontal {
        0% {
            -webkit-transform: scale3d(1, 1, 1);
                    transform: scale3d(1, 1, 1);
        }
        30% {
            -webkit-transform: scale3d(1.25, 0.75, 1);
                    transform: scale3d(1.25, 0.75, 1);
        }
        40% {
            -webkit-transform: scale3d(0.75, 1.25, 1);
                    transform: scale3d(0.75, 1.25, 1);
        }
        50% {
            -webkit-transform: scale3d(1.15, 0.85, 1);
                    transform: scale3d(1.15, 0.85, 1);
        }
        65% {
            -webkit-transform: scale3d(0.95, 1.05, 1);
                    transform: scale3d(0.95, 1.05, 1);
        }
        75% {
            -webkit-transform: scale3d(1.05, 0.95, 1);
                    transform: scale3d(1.05, 0.95, 1);
        }
        100% {
            -webkit-transform: scale3d(1, 1, 1);
                    transform: scale3d(1, 1, 1);
        }
    }

    @keyframes jello-horizontal {
        0% {
            -webkit-transform: scale3d(1, 1, 1);
                    transform: scale3d(1, 1, 1);
        }
        30% {
            -webkit-transform: scale3d(1.25, 0.75, 1);
                    transform: scale3d(1.25, 0.75, 1);
        }
        40% {
            -webkit-transform: scale3d(0.75, 1.25, 1);
                    transform: scale3d(0.75, 1.25, 1);
        }
        50% {
            -webkit-transform: scale3d(1.15, 0.85, 1);
                    transform: scale3d(1.15, 0.85, 1);
        }
        65% {
            -webkit-transform: scale3d(0.95, 1.05, 1);
                    transform: scale3d(0.95, 1.05, 1);
        }
        75% {
            -webkit-transform: scale3d(1.05, 0.95, 1);
                    transform: scale3d(1.05, 0.95, 1);
        }
        100% {
            -webkit-transform: scale3d(1, 1, 1);
                    transform: scale3d(1, 1, 1);
        }
    }

    .blink-1 {
        font-size: 50px;
        -webkit-animation: blink-1 1s both;
                animation: blink-1 1s both;
    }

    @-webkit-keyframes blink-1 {
        0%,
        50%,
        100% {
            opacity: 1;
        }
        25%,
        75% {
            opacity: 0;
        }
        }
        @keyframes blink-1 {
        0%,
        50%,
        100% {
            opacity: 1;
        }
        25%,
        75% {
            opacity: 0;
        }
    }
`;

    constructor(){
        console.log("constructor")
        super();
        const shadow = this.attachShadow({mode:"open"})
        this.couleur = this.getAttribute("couleur");
        this.text = this.getAttribute("text");
        console.log("couleur = " + this.couleur);
    }

    connectedCallback(){
        console.log("connectedCallback")
        this.shadowRoot.innerHTML = `<style>${this.style}</style>` + this.html;
        this.body = this.shadowRoot.querySelector("#body");
        this.logo = this.shadowRoot.querySelector("#logo");
        this.logo.addEventListener("click", () => {
            console.log("Logo clické");
        })
        this.logo.style.color = this.couleur;
        this.logo.textContent = this.text;

        this.shadowRoot.querySelector("#colorSelect").addEventListener("input", (event) => {
            console.log(event.target.value);
            this.logo.style.color = event.target.value;
        })

        this.shadowRoot.querySelector("#borderSelect").addEventListener("input", (event) => {
            console.log(event.target.value);
            this.logo.style.textShadow = "2px 2px"+event.target.value;
        })

        this.input = this.shadowRoot.querySelector("#logoInputText");

        this.shadowRoot.querySelector("#valider").addEventListener("click", (event) => {
            console.log(this.input.value);
            this.changeText(this.input.value);
            this.logo.classList = "text-focus-in";
        })

       this.shadowRoot.querySelector("#slider").addEventListener("click", (event) => {
            console.log(event.target.value);
            this.logo.style.fontSize = event.target.value;
            this.logo.classList = "jello-horizontal";
        })

        this.shadowRoot.querySelector("#style").addEventListener("click", (event) => {
            console.log(event.target.value);
            this.logo.style.textDecoration = event.target.value;
            this.logo.classList = "blink-1";
        })

        this.imageLink = this.shadowRoot.querySelector("#logoImage");
        this.image = this.shadowRoot.querySelector("#image")
        this.shadowRoot.querySelector("#importer").addEventListener("click", (event) => {
            console.log(this.imageLink.value);
            this.image.setAttribute("src",this.imageLink.value);
        })
    }

    changeText(newText) {
        this.logo.textContent = newText;
    }
}

customElements.define("my-logo", MyLogo);