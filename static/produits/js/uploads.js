$(document).ready(function() {
  if (window.File && window.FileList && window.FileReader) {
    $("#files").on("change", function(e) {
      var files = e.target.files,
        filesLength = files.length;
      for (var i = 0; i < 3; i++) {
        var f = files[i]
        var fileReader = new FileReader();
        fileReader.onload = (function(e) {
          var file = e.target;
          $("<span class=\"pip\">" +
            "<img class=\"imageThumb\" src=\"" + e.target.result + "\" title=\"" + file.name + "\"/>" +
            "<br/><span class=\"remove\">Remove image</span>" +
            "</span>").insertAfter("#files");
          $(".remove").click(function(){
            $(this).parent(".pip").remove();
          });
        });
        fileReader.readAsDataURL(f);
      }
    });
  } else {
    alert("Votre navigateur ne supporte pas ce format !")
  }
});


var tchaussure = document.getElementById("tchaussure");
var tvetements = document.getElementById("tvetements");
var tautre = document.getElementById("tautre");
var taille_vetements = document.getElementById("taille_vetements");
var taille_chaussure = document.getElementById("taille_chaussure");
var autre_taille = document.getElementById("autre_taille");
var mvetements = document.getElementById("mvetements");
var mvoiture = document.getElementById("mvoiture");
var melectronique = document.getElementById("melectronique");
var marque_electronique = document.getElementById("marque_electronique");
var marque_vetements = document.getElementById("marque_vetements");
var marque_voiture = document.getElementById("marque_voiture");
var taille = document.getElementById("taille");
var marque = document.getElementById("marque");

taille.addEventListener("click",function(){
  if (tvetements.checked == true){
    taille_vetements.style.display = "block";
    taille_chaussure.style.display = "none";
    autre_taille.style.display = "none";
  }
  if(tchaussure.checked == true){
    taille_chaussure.style.display = "block";
    taille_vetements.style.display = "none";
    autre_taille.style.display = "none"
  }
  if(tautre.checked == true){
    autre_taille.style.display = "block";
    taille_vetements.style.display = "none";
    taille_chaussure.style.display = "none";
  }
})

marque.addEventListener("click",function(){
  if (mvetements.checked == true){
    marque_vetements.style.display = "block";
    marque_electronique.style.display = "none";
    marque_voiture.style.display = "none";
  }
  if(mvoiture.checked == true){
    marque_voiture.style.display = "block";
    marque_vetements.style.display = "none";
    marque_electronique.style.display = "none";
  }
  if (melectronique.checked == true){
    marque_electronique.style.display = "block";
    marque_vetements.style.display = "none";
    marque_voiture.style.display = "none";
  }
})

