
var showStudentsForm = document.getElementById('addStudentFormButton');
var studentsForm = document.getElementById('studentsFormWrapper');

showStudentsForm.addEventListener('click', function(e){
	
	if (studentsForm.classList.contains("hidden")){
		studentsForm.classList.remove("hidden");
		console.log("la saca");
	} else {
		studentsForm.classList.add("hidden");
		console.log("la agrega");
	}
});