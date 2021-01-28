class MyLogo extends HTMLElement {
    html = `
    <h3  id="logo">mon logo</h3>
    <br>
    <input type="color" id="colorSelect"> `;
    
    style = `
    #logo {
        color:red;
    }`;

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
        this.myLogo = this.shadowRoot.querySelector("#logo");
        this.myLogo.addEventListener("click", () => {
            console.log("Logo clické");
        })
        this.myLogo.style.color = this.couleur;
        this.myLogo.textContent = this.text;

        this.shadowRoot.querySelector("#colorSelect").addEventListener("input", (event) => {
            console.log(event.target.value);
            this.myLogo.style.color = event.target.value;
        })
    }

    changeText(newText) {
        this.myLogo.textContent = newText;
    }
}

customElements.define("my-logo", MyLogo);