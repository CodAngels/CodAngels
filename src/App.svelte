<script>
  	let time = new Date();
  	let hour = time.getHours();
  	let minute = Math.floor(time.getMinutes() / 15) * 15;
	let week = ["Sun", "Mon","Tue", "Wed","Thu","Frid", "Sat"];
	let dayIndex = 0;
	let day = week[dayIndex];
	let selectedTimes = [];
	
	const incrementDay = () => {
    dayIndex = (dayIndex + 1) % 7;
    day = week[dayIndex];
    updateTime();
  };
	
	const decrementDay = () => {
    dayIndex = (dayIndex - 1+7) % 7;
    day = week[dayIndex];
    updateTime();
  };

  const incrementHour = () => {
    if (hour === 23) {
      hour = 0;
    } else {
      hour++;
    }
    updateTime();
  };

  const decrementHour = () => {
    if (hour === 0) {
      hour = 23;
    } else {
      hour--;
    }
    updateTime();
  };

  const incrementMinute = () => {
    if (minute === 45) {
      minute = 0;
      incrementHour();
    } else {
      minute += 15;
    }
    updateTime();
  };
	const decrementMinute = () => {
    if (minute === 0) {
      minute = 45;
      decrementHour();
    } else {
      minute -= 15;
    }
    updateTime();
  };
  const updateTime = () => {
    time.setHours(hour);
    time.setMinutes(minute);
		time.setDate(time.getDate() + (dayOfWeek - time.getDay() + 7) % 7);
  };
	function addToSelected() {
    const selected = `${day}  ${hour < 10 ? `0${hour}` : hour}:${minute < 10 ? `0${minute}` : minute}`;
    if (!selectedTimes.includes(selected)) {
    selectedTimes = [...selectedTimes, selected];
  }
  }
	function deleteTime(time) {
  	selectedTimes = selectedTimes.filter(t => t !== time);
	}
	function clearSelectedTimes() {
    	selectedTimes = [];
  }
</script>
<main >
	<div class="container">
		<h2><center>Meeting Name: CS178 Week 53 Meeting</center></h2>
		<h3 class="selectPrompt">Select Availability(30-min Slots, 24hr clock System)</h3>
		<div class="time-picker">
			<div class="hour-hand">
				<button on:click={decrementHour}>▲</button>
					<span>{hour < 10 ? `0${hour}` : hour}</span>
				<button on:click={incrementHour}>▼</button>
			</div>
			<div class="minute-hand">
				<button on:click={decrementMinute}>▲</button>
					<span>{minute < 10 ? `0${minute}` : minute}</span>
				<button on:click={incrementMinute}>▼</button>
			</div>
			<div class="day-picker">
				<button on:click={decrementDay}>◄</button>
					<span>{day < 10 ? `0${day}` : day}</span>
				<button on:click={incrementDay}>►</button>
			</div>
			<button class="available" on:click={addToSelected}>Available</button>
		</div>
		<h3 class="TimeSlot">Time Slots Selected</h3>
		<div class="selectedTimes">
			{#each selectedTimes as time}
				<div key={time}>{time}
					<button on:click={() => deleteTime(time)}>Delete</button>
				</div>
			{/each}
		</div>
		<div class="bottom-buttons">
			<button class="submit" on:click={() => {selectedTimes = []}}>Submit</button>
		</div>
	</div>
</main>
	
<style>
	.container{
		position: relative;
    	height: 700px; 
    	overflow: auto;
	}
 	.time-picker {
    	display: flex;
    	align-items: center;
    	gap: 1rem;
	  	position: absolute;
  		top: 30%;
    	left: 30%;
    	transform: translate(-50%, -50%);
  	}

  	.hour-hand,
  	.minute-hand {
    	display: flex;
    	flex-direction: column;
    	align-items: center;
    	gap: 0.5rem;
  	}
	.selectPrompt {
		position: relative;
  		bottom: 100;
  		left: 20%;
  		margin: 25px;
		overflow-y: auto;
	}
	.TimeSlot{
		display: flex;
    	align-items: center;
    	gap: 1rem;
	 	position: absolute;
  		top: 40%;
    	left: 33%;
    	transform: translate(-80%, 140%);
	}
	.selectedTimes{
    align-items: down;
    gap: 1rem;
	  position: absolute;
  	top: 60%;
    left: 32%;
    transform: translate(-80%, 0%);
	}

  button {
    font-size: 1rem;
    padding: 0.25rem 0.5rem;
    border-radius: 0.25rem;
    border: 1px solid #ccc;
    background-color: white;
    cursor: pointer;
  }
	.bottom-buttons {
  	position: fixed;
  	bottom: 0;
  	left: 50%;
  	margin: 20px;
		overflow-y: auto;
	}
	.available{
		position: fixed;
  	bottom: 22;
  	left: 59%;
  	margin: 110px;
		background-color:green;
	}
  button:focus {
    outline: none;
  }
  span {
    font-size: 1.5rem;
    font-weight: bold;
  }
</style>