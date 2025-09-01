#  HospiHelp – Hospital Assistance System

HospiHelp is a **Python + MySQL-based hospital management project** that allows doctors, patients, and chemists to interact with a hospital system.  
It provides appointment booking, emergency support, a medi-store, and nurse hiring features.

---

##  Features

###  Doctor Module
- Secure login with name verification and password riddle.
- View appointments with patients.
- Allot time slots to patients.
- Delete or search patient records.
- Access nurse details.

###  Patient Module
- **Emergency Help**  
  - Call an ambulance with simulated vehicle & contact details.  
  - Locate nearest hospitals.  
  - Safety procedure manual for first aid.  

- **First Aid Section**  
  - Step-by-step guide for handling small burns.

- **Appointment Booking**  
  - View available doctors and their specializations.  
  - Select hospital, doctor, and time slot.  
  - Confirm and register appointment in the database.  

- **MediStore (Pharmacy System)**  
  - Patients can order medicines (stock automatically updated).  
  - Chemists can login and manage inventory (add, update, delete medicines).  

- **Hire a Nurse**  
  - Browse available nurses with specialization and costs.  
  - Book a nurse with appointment details (date, state, address).  

---

## 🛠️ Tech Stack

- **Language:** Python 3  
- **Database:** MySQL  
- **Modules Used:**
  - `mysql.connector`
  - `random`
  - `datetime`
  - `time`  

---

##  Database Structure

### `Bookings` Table
| Column             | Type          |
|---------------------|--------------|
| SerialNo (PK)       | int (Auto Increment) |
| Name                | varchar(25)  |
| Age                 | char(2)      |
| Gender              | char(1)      |
| Hospital            | varchar(25)  |
| Specialist          | varchar(25)  |
| DayOfAppointment    | varchar(10)  |
| DateOfAppointment   | varchar(20)  |
| TimeAllotedInPM     | varchar(20)  |
| DoctorName          | varchar(25)  |

Other tables used include:  
- `doctor`
- `medistore`
- `hireNurse`
- `nurse`

---

## 📖 Example Workflows

- A patient books an appointment:  
  1. Enter personal details.  
  2. Choose doctor & hospital.  
  3. Select a time slot.  
  4. Appointment saved in the database.  

- A chemist logs in:  
  1. Manage medicines (add/update/delete).  
  2. View available medicines.  
  3. Patients can order and stock auto-updates.  

---

##  Future Improvements
- Add GUI (Tkinter/Flask/Django).  
- Improve authentication (hashed passwords).  
- Online payment integration for appointments and medicines.  
- SMS/Email notifications for bookings.  

---

##  Author
Project developed by **Anant Jain** (XII Aquila).  
