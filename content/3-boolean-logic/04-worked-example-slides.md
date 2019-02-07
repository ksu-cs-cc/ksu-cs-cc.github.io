---
type: "reveal"
hidden: true
---

<section>
  <p>A program should turn the lights on if the light switch in the room is in the “ON” position. Similarly, it should turn on the lights if it detects there are people in the room using a motion sensor, regardless of whether the light switch is “ON” or "OFF". However, it should respect a master switch, such that if the master switch is off, the lights can not be turned on at all.<p>
</section>
<section>
	<table class="reveal" style="font-size: 0.8em">
		<tr>
			<th>Switch A</th>
			<th>Motion B</th>
			<th>Master C</th>
			<th>Output</th>
		</tr>
		<tr>
			<td>F</td>
			<td>F</td>
			<td>F</td>
			<td>F</td>
		</tr>
		<tr>
			<td>F</td>
			<td>F</td>
			<td>T</td>
			<td>F</td>
		</tr>
		<tr>
			<td>F</td>
			<td>T</td>
			<td>F</td>
			<td>F</td>
		</tr>
		<tr style="font-weight: bold; color: #512888">
			<td>F</td>
			<td>T</td>
			<td>T</td>
			<td>T</td>
		</tr>
		<tr>
			<td>T</td>
			<td>F</td>
			<td>F</td>
			<td>F</td>
		</tr>
		<tr style="font-weight: bold; color: #512888">
			<td>T</td>
			<td>F</td>
			<td>T</td>
			<td>T</td>
		</tr>
		<tr>
			<td>T</td>
			<td>T</td>
			<td>F</td>
			<td>F</td>
		</tr>
		<tr style="font-weight: bold; color: #512888">
			<td>T</td>
			<td>T</td>
			<td>T</td>
			<td>T</td>
		</tr>
  </table>
</section>
<section>
	<h3>Motion Sensor ∧ Master</h3>
	<img class="stretch plain" src="/images/boolean_worked_a.png">
</section>
<section>
	<h3>Light Switch ∧ Master</h3>
	<img class="stretch plain" src="/images/boolean_worked_b.png">
</section>
<section>
	<h3>Light Switch ∧ Motion Sensor ∧ Master</h3>
	<img class="stretch plain" src="/images/boolean_worked_c.png">
</section>
<section>
	<h3>Output</h3>
	<img class="stretch plain" src="/images/boolean_worked_d.png">
</section>
<section>
	<h3>A ∧ C</h3>
	<img class="stretch plain" src="/images/boolean_worked_e.png">
</section>
<section>
	<h3>B ∧ C</h3>
	<img class="stretch plain" src="/images/boolean_worked_f.png">
</section>
<section>
	<h3>(A ∧ C) ? (B ∧ C)</h3>
	<img class="stretch plain" src="/images/boolean_worked_g.png">
</section>
<section>
	<h3>(A ∧ C) ∨ (B ∧ C)</h3>
	<img class="stretch plain" src="/images/boolean_worked_g.png">
</section>
<section>
	<h4>(Light Switch ∧ Master Switch)<br>∨<br>(Motion Sensor ∧ Master Switch)</h4>
</section>
<section>
	<table class="reveal" style="font-size: 0.8em">
		<tr>
			<th>Switch A</th>
			<th>Motion B</th>
			<th>Master C</th>
			<th>Output</th>
		</tr>
		<tr>
			<td>F</td>
			<td>F</td>
			<td>F</td>
			<td>F</td>
		</tr>
		<tr>
			<td>F</td>
			<td>F</td>
			<td>T</td>
			<td>F</td>
		</tr>
		<tr>
			<td>F</td>
			<td>T</td>
			<td>F</td>
			<td>F</td>
		</tr>
		<tr style="font-weight: bold; color: #512888">
			<td>F</td>
			<td>T</td>
			<td>T</td>
			<td>T</td>
		</tr>
		<tr>
			<td>T</td>
			<td>F</td>
			<td>F</td>
			<td>F</td>
		</tr>
		<tr style="font-weight: bold; color: #512888">
			<td>T</td>
			<td>F</td>
			<td>T</td>
			<td>T</td>
		</tr>
		<tr>
			<td>T</td>
			<td>T</td>
			<td>F</td>
			<td>F</td>
		</tr>
		<tr style="font-weight: bold; color: #512888">
			<td>T</td>
			<td>T</td>
			<td>T</td>
			<td>T</td>
		</tr>
  </table>
</section>
<section>
	<table class="reveal" style="font-size: 0.8em">
		<tr>
			<th>Switch A</th>
			<th>Motion B</th>
			<th>Master C</th>
			<th>Output</th>
		</tr>
		<tr style="font-weight: bold; color: #512888">
			<td>F</td>
			<td>T</td>
			<td>T</td>
			<td>T</td>
		</tr>
		<tr style="font-weight: bold; color: #512888">
			<td>T</td>
			<td>F</td>
			<td>T</td>
			<td>T</td>
		</tr>
		<tr style="font-weight: bold; color: #512888">
			<td>T</td>
			<td>T</td>
			<td>T</td>
			<td>T</td>
		</tr>
  </table>
	<p style="font-size: 1.5em">(¬A ∧ B ∧ C)<br>∨ (A ∧ ¬B ∧ C)<br>∨ (A ∧ B ∧ C)</p>
</section>
<section>
  <p style="font-size: 1.5em">(¬A ∧ B ∧ C)<br>∨ (A ∧ ¬B ∧ C)<br>∨ (A ∧ B ∧ C)</p>
</section>
<section>
  <p style="font-size: 1.5em">(¬A ∧ B ∧ C)<br>∨ (A ∧ ¬B ∧ C)<br>∨ (A ∧ B ∧ C)<br><mark>∨ (A ∧ B ∧ C)</mark></p>
</section>
<section>
  <p style="font-size: 1.5em">(¬A ∧ B ∧ C)<br><mark>∨ (A ∧ B ∧ C)</mark><br>∨ (A ∧ ¬B ∧ C)<br>∨ (A ∧ B ∧ C)</p>
</section>
<section>
  <p style="font-size: 1.5em">(¬A ∧ B ∧ C)<br>∨ (A ∧ B ∧ C)<br>∨ (<mark>¬B ∧ A</mark> ∧ C)<br>∨ (<mark>B ∧ A</mark> ∧ C)</p>
</section>
<section>
  <p style="font-size: 1.5em; line-height: 1.55em"><span style="font-size: 1.7em">(</span><span style="font-size: 1.3em">(</span>¬A ∧ (B ∧ C)<span style="font-size: 1.3em">)</span><br>∨ <span style="font-size: 1.3em">(</span>A ∧ (B ∧ C)<span style="font-size: 1.3em">)</span><span style="font-size: 1.7em">)</span><br>∨<br><span style="font-size: 1.7em">(</span><span style="font-size: 1.3em">(</span>¬B ∧ (A ∧ C)<span style="font-size: 1.3em">)</span><br>∨ <span style="font-size: 1.3em">(</span>B ∧ (A ∧ C)<span style="font-size: 1.3em">)</span><span style="font-size: 1.7em">)</span></p>
</section>
<section>
  <p style="font-size: 1.5em; line-height: 1.55em"><span style="font-size: 1.7em">(</span><span style="font-size: 1.3em">(</span>¬A ∧ <mark>(B ∧ C)</mark><span style="font-size: 1.3em">)</span><br>∨ <span style="font-size: 1.3em">(</span>A ∧ <mark>(B ∧ C)</mark><span style="font-size: 1.3em">)</span><span style="font-size: 1.7em">)</span><br>∨<br><span style="font-size: 1.7em">(</span><span style="font-size: 1.3em">(</span>¬B ∧ (A ∧ C)<span style="font-size: 1.3em">)</span><br>∨ <span style="font-size: 1.3em">(</span>B ∧ (A ∧ C)<span style="font-size: 1.3em">)</span><span style="font-size: 1.7em">)</span></p>
</section>
<section>
  <p style="font-size: 1.5em; line-height: 1.55em"><mark><span style="font-size: 1.3em">(</span>(B ∧ C) ∧ (¬A ∨ A)<span style="font-size: 1.3em">)</span></mark><br>∨<br><span style="font-size: 1.7em">(</span><span style="font-size: 1.3em">(</span>¬B ∧ (A ∧ C)<span style="font-size: 1.3em">)</span><br>∨ <span style="font-size: 1.3em">(</span>B ∧ (A ∧ C)<span style="font-size: 1.3em">)</span><span style="font-size: 1.7em">)</span></p>
</section>
<section>
  <p style="font-size: 1.5em; line-height: 1.55em"><mark><span style="font-size: 1.3em">(</span>(B ∧ C) ∧ (¬A ∨ A)<span style="font-size: 1.3em">)</span></mark><br>∨<br><span style="font-size: 1.7em">(</span><span style="font-size: 1.3em">(</span>¬B ∧ <mark>(A ∧ C)</mark><span style="font-size: 1.3em">)</span><br>∨ <span style="font-size: 1.3em">(</span>B ∧ <mark>(A ∧ C)</mark><span style="font-size: 1.3em">)</span><span style="font-size: 1.7em">)</span></p>
</section>
<section>
  <p style="font-size: 1.5em; line-height: 1.55em"><span style="font-size: 1.3em">(</span>(B ∧ C) ∧ (¬A ∨ A)<span style="font-size: 1.3em">)</span><br>∨<br><mark><span style="font-size: 1.3em">(</span>(A ∧ C) ∧ (¬B ∨ B)<span style="font-size: 1.3em">)</span></mark></p>
</section>
<section>
  <p style="font-size: 1.5em; line-height: 1.55em"><span style="font-size: 1.3em">(</span>(B ∧ C) ∧ <mark>(¬A ∨ A)</mark><span style="font-size: 1.3em">)</span><br>∨<br><span style="font-size: 1.3em">(</span>(A ∧ C) ∧ <mark>(¬B ∨ B)</mark><span style="font-size: 1.3em">)</span></p>
</section>
<section>
  <p style="font-size: 1.5em; line-height: 1.55em"><span style="font-size: 1.3em">(</span>(B ∧ C) ∧ <mark>T</mark><span style="font-size: 1.3em">)</span><br>∨<br><span style="font-size: 1.3em">(</span>(A ∧ C) ∧ <mark>T</mark><span style="font-size: 1.3em">)</span></p>
</section>
<section>
  <p style="font-size: 1.5em; line-height: 1.55em"><span style="font-size: 1.3em">(</span>(B ∧ C) <mark>∧ T</mark><span style="font-size: 1.3em">)</span><br>∨<br><span style="font-size: 1.3em">(</span>(A ∧ C) <mark>∧ T</mark><span style="font-size: 1.3em">)</span></p>
</section>
<section>
  <p style="font-size: 1.5em; line-height: 1.55em">(B ∧ C)<br>∨<br>(A ∧ C)</p>
</section>
<section>
	<h4>(Motion Sensor ∧ Master Switch)<br>∨<br>(Light Switch ∧ Master Switch)</h4>
</section>
<section>
	<h4>(Master Switch)<br>∧<br>(Light Switch ∨ Motion Sensor)</h4>
</section>
