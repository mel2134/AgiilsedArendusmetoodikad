class Patient{
    constructor(name,age){
        this.name = name
        this.age = age
    }
}
class Doctor{
    constructor(name,age,prof,times){
        this.name = name
        this.age = age
        this.prof = prof
        this.times = times
    }
}
class Hospital{
    constructor(){
        this.patients = []
        this.doctors = []
    }
    showAllPatients(){
        for(let i = 0;i<this.patients.length;i++){
            console.log(this.patients[i])
        }
    }
    showAllDoctors(){
        for(let i = 0;i<this.doctors.length;i++){
            console.log(this.doctors[i])
        }
    }
    showDoctorTime(){
        let name2 = prompt("What doctor?: ")
        let doc = this.doctors.find(({ name }) => name === name2)
        console.log(doc.times)
        let time = prompt("Meetup at: ")
        let index = doc.times.indexOf(time)
        if (index == -1){
            console.log("no such timw")
        }
        doc.times.splice(index, 1)
        console.log("Meeting up at " + time)
        
        
        
    }
}
const hospital = new Hospital()
hospital.patients.push(new Patient("pat1",5))
hospital.patients.push(new Patient("pat2",123213))
hospital.patients.push(new Patient("pat3",12))
hospital.patients.push(new Patient("pat4",124))

hospital.doctors.push(new Doctor("doctor1",58,"Perearst",["13:00","03:00"]))
hospital.doctors.push(new Doctor("doctor2",51,"Kõrvaarst",["12:00","03:00"]))
hospital.doctors.push(new Doctor("doctor3",544,"Kirurg",["03:00","04:00"]))
hospital.showAllPatients()
hospital.showAllDoctors()
hospital.showDoctorTime()
hospital.showAllDoctors()
