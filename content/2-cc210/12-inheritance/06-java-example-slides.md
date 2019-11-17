---
type: "reveal"
hidden: true
---

<section>
	<h2>Problem Statement</h2>
</section>
<section>
  <ol style="font-size: .45em">
    <li>When the program is executed, a single command-line argument should be provided. That argument will be the path to a file containing descriptions for each tool in the toolbox. If the argument is not provided, or the input file cannot be successfully read or parsed, the program should print "Invalid Input" and terminate.</li>
    <li>The input file will contain at least two lines of input. The first line will give the number of tools included in the input file as an integer. Each subsequent line will identify a particular tool using the name of the class representing the tool, followed by values for each attribute of the tool. The values will be separated by spaces, and listed in the same order as those attributes are accepted in the tool's constructor.</li>
    <li>Once the input is read, the program will then accept a query as input via the terminal. That input should consist of multiple parts on a single line, separated by a space. The first part will be the name of an action that needs to be performed, and then following that will be one or more values to be provided to that action as arguments, separated by spaces.</li>
    <li>The program will review its list of available tools, finding any tool that supports that action. It will then call the method in that tool that corresponds with the action (the method and action names will be the same), providing the values as an arguments. If the tool responds with true to that method call, then that tool is able to perform that action. The program should print the description of the appropriate tool to the terminal and terminate. In this example, each query will only result in one matching tool, if any.</li>
    <li>If a matching tool cannot be found, or there is any errors reading the input from the terminal, the program should print "Invalid Tool" and terminate.</li>
  </ol>
</section>
<section>
  <h2>Head &rarr; Desk</h2>
	<img class="stretch plain" src="https://media.giphy.com/media/HlqvH9JrahLZ6/source.gif">
  <p class="imagecredit">Image Credit: <a href="https://media.giphy.com/media/HlqvH9JrahLZ6">Giphy</a></p>
	<p>Let's break it down into classes</p>
</section>

<section>
  <img class="stretch plain" src="/images/12.7.j.8.uml.png">
</section>

<section>
  <div style="float: right; width: 30%">
    <img class="plain" style="width: 100%" src="/images/12.7.j.8.tool.png">
  </div>
  <div style="width: 70%">
    <pre class="stretch" style="font-size: .35em"><code class="java">public abstract class Tool{

  protected Tool(){
    // do nothing
  }

  public abstract String describe();

}</code></pre>
  </div>
</section>


<section>
  <div style="float: right; width: 30%">
    <img class="plain" style="width: 100%" src="/images/12.7.j.8.wrench.png">
  </div>
  <div style="width: 70%">
    <pre class="stretch" style="font-size: .35em"><code class="java">public abstract class Wrench extends Tool{

  private int length;

  protected Wrench(int length){
    this.length = length;
  }

  public int getLength(){ return this.length; }

  public abstract boolean tighten(int clearance, int size);

}</code></pre>
  </div>
</section>


<section>
  <div style="float: right; width: 30%">
    <img class="plain" style="width: 100%" src="/images/12.7.j.8.saw.png">
  </div>
  <div style="width: 70%">
    <pre class="stretch" style="font-size: .35em"><code class="java">public abstract class Saw extends Tool{

  private int length;

  protected Saw(int length){
    this.length = length;
  }

  public int getLength(){ return this.length; }

  public abstract boolean cut(int length, String material);

}</code></pre>
  </div>
</section>


<section>
  <img class="stretch plain" src="/images/stop.png">
  <h3>Check Structure!</h3>
</section>

<section>
  <div style="float: right; width: 30%">
    <img class="plain" style="width: 100%" src="/images/12.7.j.8.aj.png">
  </div>
  <div style="width: 70%">
    <pre class="stretch" style="font-size: .32em"><code class="java">public class AdjustableWrench extends Wrench{

  private int min_size;
  private int max_size;

  public AdjustableWrench(int length, int min_size, int max_size){
    super(length);
    this.min_size = min_size;
    this.max_size = max_size;
  }

  public int getMinSize(){ return this.min_size; }
  public int getMaxSize(){ return this.max_size; }

  // other methods go here

}</code></pre>
  </div>
</section>


<section>
  <div style="float: right; width: 30%">
    <img class="plain" style="width: 100%" src="/images/12.7.j.8.aj.png">
  </div>
  <div style="width: 70%">
    <pre class="stretch" style="font-size: .32em"><code class="java">public class AdjustableWrench extends Wrench{

  private int min_size;
  private int max_size;

  public AdjustableWrench(int length, int min_size, int max_size){
    super(length);
    this.min_size = min_size;
    this.max_size = max_size;
  }

  public int getMinSize(){ return this.min_size; }
  public int getMaxSize(){ return this.max_size; }

  public String describe(){
    return String.format("AdjustableWrench: Length: %d MinSize: %d
      MaxSize: %d", this.length, this.min_size, this.max_size);
  }

  // other methods go here

}</code></pre>
  </div>
</section>


<section>
  <div style="float: right; width: 30%">
    <img class="plain" style="width: 100%" src="/images/12.7.j.8.aj.png">
  </div>
  <div style="width: 70%">
    <pre class="stretch" style="font-size: .32em"><code class="java">public class AdjustableWrench extends Wrench{

  private int min_size;
  private int max_size;

  public AdjustableWrench(int length, int min_size, int max_size){
    super(length);
    this.min_size = min_size;
    this.max_size = max_size;
  }

  public int getMinSize(){ return this.min_size; }
  public int getMaxSize(){ return this.max_size; }

  public String describe(){
    return String.format("AdjustableWrench: Length: %d MinSize: %d
      MaxSize: %d", <mark>this.length</mark>, this.min_size, this.max_size);
  }

  // other methods go here

}</code></pre>
  </div>
</section>


<section>
  <div style="float: right; width: 30%">
    <img class="plain" style="width: 100%" src="/images/12.7.j.8.aj.png">
  </div>
  <div style="width: 70%">
    <pre class="stretch" style="font-size: .32em"><code class="java">public class AdjustableWrench extends Wrench{

  private int min_size;
  private int max_size;

  public AdjustableWrench(int length, int min_size, int max_size){
    super(length);
    this.min_size = min_size;
    this.max_size = max_size;
  }

  public int getMinSize(){ return this.min_size; }
  public int getMaxSize(){ return this.max_size; }

  public String describe(){
    return String.format("AdjustableWrench: Length: %d MinSize: %d
      MaxSize: %d", <mark style="background-color: red">this.length</mark>, this.min_size, this.max_size);
  }

  // other methods go here

}</code></pre>
  </div>
</section>


<section>
  <div style="float: right; width: 30%">
    <img class="plain" style="width: 100%" src="/images/12.7.j.8.aj.png">
  </div>
  <div style="width: 70%">
    <pre class="stretch" style="font-size: .32em"><code class="java">public class AdjustableWrench extends Wrench{

  private int min_size;
  private int max_size;

  public AdjustableWrench(int length, int min_size, int max_size){
    super(length);
    this.min_size = min_size;
    this.max_size = max_size;
  }

  public int getMinSize(){ return this.min_size; }
  public int getMaxSize(){ return this.max_size; }

  public String describe(){
    return String.format("AdjustableWrench: Length: %d MinSize: %d
      MaxSize: %d", <mark>this.getLength()</mark>, this.min_size, this.max_size);
  }

  // other methods go here

}</code></pre>
  </div>
</section>


<section>
  <div style="float: right; width: 30%">
    <img class="plain" style="width: 100%" src="/images/12.7.j.8.aj.png">
  </div>
  <div style="width: 70%">
    <pre class="stretch" style="font-size: .32em"><code class="java">public class AdjustableWrench extends Wrench{

  private int min_size;
  private int max_size;

  public AdjustableWrench(int length, int min_size, int max_size){
    super(length);
    this.min_size = min_size;
    this.max_size = max_size;
  }

  public int getMinSize(){ return this.min_size; }
  public int getMaxSize(){ return this.max_size; }

  public String describe(){
    return String.format("AdjustableWrench: Length: %d MinSize: %d
      MaxSize: %d", this.getLength(), this.min_size, this.max_size);
  }

  // other methods go here

}</code></pre>
  </div>
</section>

<section>
  <h3>Adjustable Wrench</h3>
  <img class="stretch plain" src="/images/12.7.x.8.adjustable_wiki.png">
</section>

<section>
  <div style="float: right; width: 30%">
    <img class="plain" style="width: 100%" src="/images/12.7.j.8.aj.png">
  </div>
  <div style="width: 70%">
    <pre class="stretch" style="font-size: .32em"><code class="java">public class AdjustableWrench extends Wrench{

  private int min_size;
  private int max_size;

  public AdjustableWrench(int length, int min_size, int max_size){
    super(length);
    this.min_size = min_size;
    this.max_size = max_size;
  }

  public int getMinSize(){ return this.min_size; }
  public int getMaxSize(){ return this.max_size; }

  public String describe(){
    return String.format("AdjustableWrench: Length: %d MinSize: %d
      MaxSize: %d", this.getLength(), this.min_size, this.max_size);
  }

  public boolean tighten(int clearance, int size){
    return clearance >= this.getLength() && size >= this.min_size
      && size <= this.max_size;
  }
}</code></pre>
  </div>
</section>

<section>
  <h3>Combination Wrench</h3>
  <img class="stretch plain" src="/images/12.7.x.8.combination_wiki.jpg">
</section>

<section>
  <div style="float: right; width: 30%">
    <img class="plain" style="width: 100%" src="/images/12.7.j.8.co.png">
  </div>
  <div style="width: 70%">
    <pre class="stretch" style="font-size: .32em"><code class="java">public class CombinationWrench extends Wrench{

  private int size;

  public CombinationWrench(int length, int size){
    super(length);
    this.size = size;
  }

  public int getSize(){ return this.size; }

  public String describe(){
    return String.format("CombinationWrench Length: %d Size: %d",
        this.getLength(), this.size);
  }

  public boolean tighten(int clearance, int size){
    return clearance >= this.getLength() && size == this.size;
  }
}</code></pre>
  </div>
</section>

<section>
  <h3>Open End Wrench</h3>
  <img class="stretch plain" src="/images/12.7.x.8.openend_wiki.jpg">
</section>

<section>
  <div style="float: right; width: 30%">
    <img class="plain" style="width: 100%" src="/images/12.7.j.8.oe.png">
  </div>
  <div style="width: 70%">
    <pre class="stretch" style="font-size: .32em"><code class="java">public class OpenEndWrench extends Wrench{

  private int size_one;
  private int size_two;

  public OpenEndWrench(int length, int size_one, int size_two){
    super(length);
    this.size_one = size_one;
    this.size_two = size_two;
  }

  public int getSizeOne(){ return this.size_one; }
  public int getSizeTwo(){ return this.size_two; }

  public String describe(){
    return String.format("OpenEndWrench Length: %d SizeOne: %d
          SizeTwo: %d", this.getLength(), this.size_one,
          this.size_two);
  }

  public boolean tighten(int clearance, int size){
    return clearance >= this.getLength() &&
          (size == this.size_one || size == this.size_two);
  }
}</code></pre>
  </div>
</section>


<section>
  <img class="stretch plain" src="/images/stop.png">
  <h3>Check Structure!</h3>
</section>


<section>
  <div style="float: right; width: 30%">
    <img class="plain" style="width: 100%" src="/images/12.7.j.8.cc.png">
  </div>
  <div style="width: 70%">
    <pre class="stretch" style="font-size: .32em"><code class="java">public class CrossCutSaw extends Saw{

  private String[] materials;

  public CrossCutSaw(int length, String materials){
    super(length);
    this.materials = materials.split(":");
  }

  public String getMaterials(){
    return String.join(", ", this.materials);
  }

  public String describe(){
    return String.format("CrossCutSaw Length: %d Materials: %s",
        this.getLength(), this.getMaterials());
  }

  // additional methods here
}</code></pre>
  </div>
</section>


<section>
  <div style="float: right; width: 30%">
    <img class="plain" style="width: 100%" src="/images/12.7.j.8.cc.png">
  </div>
  <div style="width: 70%">
    <pre class="stretch" style="font-size: .32em"><code class="java">public class CrossCutSaw extends Saw{

  private String[] materials;

  public CrossCutSaw(int length, String materials){
    super(length);
    this.materials = <mark>materials.split(":")</mark>;
  }

  public String getMaterials(){
    return <mark>String.join(", ", this.materials)</mark>;
  }

  public String describe(){
    return String.format("CrossCutSaw Length: %d Materials: %s",
        this.getLength(), this.getMaterials());
  }

  // additional methods here
}</code></pre>
  </div>
</section>


<section>
  <div style="float: right; width: 30%">
    <img class="plain" style="width: 100%" src="/images/12.7.j.8.cc.png">
  </div>
  <div style="width: 70%">
    <pre class="stretch" style="font-size: .32em"><code class="java">public class CrossCutSaw extends Saw{

  private String[] materials;

  public CrossCutSaw(int length, String materials){
    super(length);
    this.materials = materials.split(":");
  }

  public String getMaterials(){
    return String.join(", ", this.materials);
  }

  public String describe(){
    return String.format("CrossCutSaw Length: %d Materials: %s",
        this.getLength(), this.getMaterials());
  }

  private boolean findMaterial(String material){
    for(String m : this.materials){
      if(m.equals(material)){
        return true;
      }
    }
    return false;
  }

}</code></pre>
  </div>
</section>


<section>
  <div style="float: right; width: 30%">
    <img class="plain" style="width: 100%" src="/images/12.7.j.8.cc.png">
  </div>
  <div style="width: 70%">
    <pre class="stretch" style="font-size: .32em"><code class="java">public class CrossCutSaw extends Saw{

  private String[] materials;

  public CrossCutSaw(int length, String materials){
    super(length);
    this.materials = materials.split(":");
  }

  public String getMaterials(){
    return String.join(", ", this.materials);
  }

  public String describe(){
    return String.format("CrossCutSaw Length: %d Materials: %s",
        this.getLength(), this.getMaterials());
  }

  private boolean findMaterial(String material){
    for(String m : this.materials){
      if(m.equals(material)){
        return true;
      }
    }
    return false;
  }

  public boolean cut(int length, String material){
    return length &lt; this.getLength() &&
          this.findMaterial(material);
  }
}</code></pre>
  </div>
</section>


<section>
  <div style="float: right; width: 30%">
    <img class="plain" style="width: 100%" src="/images/12.7.j.8.hs.png">
  </div>
  <div style="width: 70%">
    <pre class="stretch" style="font-size: .32em"><code class="java">public class HackSaw extends Saw{

  public HackSaw(int length){
    super(length);
  }

  public String describe(){
    return String.format("HackSaw Length: %d Material: metal",
        this.getLength());
  }

  public boolean cut(int length, String material){
    return length &lt; this.getLength() && material.equals("metal");
  }
}</code></pre>
  </div>
</section>


<section>
  <img class="stretch plain" src="/images/stop.png">
  <h3>Check Structure!</h3>
</section>


<section>
  <div style="float: right; width: 30%">
    <img class="plain" style="width: 100%" src="/images/12.7.j.8.m.png">
  </div>
  <div style="width: 70%">
    <pre class="stretch" style="font-size: .4em"><code class="java">import java.util.Scanner;
import java.nio.file.Paths;
import java.lang.Exception;

public class Main{

  // methods go here

}
</code></pre>
  </div>
</section>


<section>
  <div style="float: right; width: 30%">
    <img class="plain" style="width: 100%" src="/images/12.7.j.8.m.png">
  </div>
  <div style="width: 70%">
    <pre class="stretch" style="font-size: .4em"><code class="java">import java.util.Scanner;
import java.nio.file.Paths;
import java.lang.Exception;

public class Main{

  <mark>// methods go here</mark>

}
</code></pre>
  </div>
</section>


<section>
  <pre class="stretch" style="font-size: .33em"><code class="java">public static Tool[] readInput(String filename){
  try(
    Scanner scanner = new Scanner(Paths.get(filename))
  ){
    int num_tools = Integer.parseInt(scanner.nextLine());
    Tool[] tools = new Tool[num_tools];



    return tools;
  }catch(Exception e){
    System.out.println("Invalid Input");
    return new Tool[0];
  }
}</code></pre>
</section>



<section>
  <pre class="stretch" style="font-size: .33em"><code class="java">public static Tool[] readInput(String filename){
  try(
    Scanner scanner = new Scanner(Paths.get(filename))
  ){
    int num_tools = Integer.parseInt(scanner.nextLine());
    Tool[] tools = new Tool[num_tools];
    for(int i = 0; i &lt; num_tools; i++){


    }
    return tools;
  }catch(Exception e){
    System.out.println("Invalid Input");
    return new Tool[0];
  }
}</code></pre>
</section>




<section>
  <pre class="stretch" style="font-size: .33em"><code class="java">public static Tool[] readInput(String filename){
  try(
    Scanner scanner = new Scanner(Paths.get(filename))
  ){
    int num_tools = Integer.parseInt(scanner.nextLine());
    Tool[] tools = new Tool[num_tools];
    for(int i = 0; i &lt; num_tools; i++){
      String[] line = scanner.nextLine().split(" ");


    }
    return tools;
  }catch(Exception e){
    System.out.println("Invalid Input");
    return new Tool[0];
  }
}</code></pre>
</section>





<section>
  <pre class="stretch" style="font-size: .33em"><code class="java">public static Tool[] readInput(String filename){
  try(
    Scanner scanner = new Scanner(Paths.get(filename))
  ){
    int num_tools = Integer.parseInt(scanner.nextLine());
    Tool[] tools = new Tool[num_tools];
    for(int i = 0; i &lt; num_tools; i++){
      String[] line = scanner.nextLine().split(" ");

      if(line[0].equals("AdjustableWrench")){

      }else if(line[0].equals("OpenEndWrench")){

      }else if(line[0].equals("CombinationWrench")){

      }else if(line[0].equals("CrossCutSaw")){

      }else if(line[0].equals("HackSaw")){

      }else{
        throw new Exception("Unknown Tool: " + line[0]);
      }
    }
    return tools;
  }catch(Exception e){
    System.out.println("Invalid Input");
    return new Tool[0];
  }
}</code></pre>
</section>

<section>
  <pre class="stretch" style="font-size: .33em"><code class="java">public static Tool[] readInput(String filename){
  try(
    Scanner scanner = new Scanner(Paths.get(filename))
  ){
    int num_tools = Integer.parseInt(scanner.nextLine());
    Tool[] tools = new Tool[num_tools];
    for(int i = 0; i &lt; num_tools; i++){
      String[] line = scanner.nextLine().split(" ");
      int length = Integer.parseInt(line[1]);
      if(line[0].equals("AdjustableWrench")){
        int min_size = Integer.parseInt(line[2]);
        int max_size = Integer.parseInt(line[3]);
        tools[i] = new AdjustableWrench(length, min_size, max_size);
      }else if(line[0].equals("OpenEndWrench")){
        int size_one = Integer.parseInt(line[2]);
        int size_two = Integer.parseInt(line[3]);
        tools[i] = new OpenEndWrench(length, size_one, size_two);
      }else if(line[0].equals("CombinationWrench")){
        int size = Integer.parseInt(line[2]);
        tools[i] = new CombinationWrench(length, size);
      }else if(line[0].equals("CrossCutSaw")){
        tools[i] = new CrossCutSaw(length, line[2]);
      }else if(line[0].equals("HackSaw")){
        tools[i] = new HackSaw(length);
      }else{
        throw new Exception("Unknown Tool: " + line[0]);
      }
    }
    return tools;
  }catch(Exception e){
    System.out.println("Invalid Input");
    return new Tool[0];
  }
}</code></pre>
</section>


<section>
  <pre class="stretch" style="font-size: .38em"><code class="java">public static Tool findTool(Tool[] tools, String query){
  String[] query_parts = query.split(" ");


























}</code></pre>
</section>


<section>
  <pre class="stretch" style="font-size: .38em"><code class="java">public static Tool findTool(Tool[] tools, String query){
  String[] query_parts = query.split(" ");
  if(query_parts[0].equals("tighten")){











  }else if(query_parts[0].equals("cut")){










  }else{

  }
}</code></pre>
</section>


<section>
  <pre class="stretch" style="font-size: .38em"><code class="java">public static Tool findTool(Tool[] tools, String query){
  String[] query_parts = query.split(" ");
  if(query_parts[0].equals("tighten")){
    int clearance = Integer.parseInt(query_parts[1]);
    int size = Integer.parseInt(query_parts[2]);









  }else if(query_parts[0].equals("cut")){
    int length = Integer.parseInt(query_parts[1]);









  }else{

  }
}</code></pre>
</section>


<section>
  <pre class="stretch" style="font-size: .38em"><code class="java">public static Tool findTool(Tool[] tools, String query){
  String[] query_parts = query.split(" ");
  if(query_parts[0].equals("tighten")){
    int clearance = Integer.parseInt(query_parts[1]);
    int size = Integer.parseInt(query_parts[2]);
    for(Tool t : tools){






    }

  }else if(query_parts[0].equals("cut")){
    int length = Integer.parseInt(query_parts[1]);
    for(Tool t : tools){






    }

  }else{

  }
}</code></pre>
</section>


<section>
  <pre class="stretch" style="font-size: .38em"><code class="java">public static Tool findTool(Tool[] tools, String query){
  String[] query_parts = query.split(" ");
  if(query_parts[0].equals("tighten")){
    int clearance = Integer.parseInt(query_parts[1]);
    int size = Integer.parseInt(query_parts[2]);
    for(Tool t : tools){
      if(t instanceof Wrench){
        Wrench w = (Wrench)t;



      }
    }

  }else if(query_parts[0].equals("cut")){
    int length = Integer.parseInt(query_parts[1]);
    for(Tool t : tools){
      if(t instanceof Saw){
        Saw s = (Saw)t;



      }
    }

  }else{

  }
}</code></pre>
</section>


<section>
  <pre class="stretch" style="font-size: .38em"><code class="java">public static Tool findTool(Tool[] tools, String query){
  String[] query_parts = query.split(" ");
  if(query_parts[0].equals("tighten")){
    int clearance = Integer.parseInt(query_parts[1]);
    int size = Integer.parseInt(query_parts[2]);
    for(Tool t : tools){
      if(t instanceof Wrench){
        Wrench w = (Wrench)t;
        if(w.tighten(clearance, size)){
          return t;
        }
      }
    }

  }else if(query_parts[0].equals("cut")){
    int length = Integer.parseInt(query_parts[1]);
    for(Tool t : tools){
      if(t instanceof Saw){
        Saw s = (Saw)t;
        if(s.cut(length; query_parts[2]))){
          return s;
        }
      }
    }

  }else{

  }
}</code></pre>
</section>


<section>
  <pre class="stretch" style="font-size: .38em"><code class="java">public static Tool findTool(Tool[] tools, String query){
  String[] query_parts = query.split(" ");
  if(query_parts[0].equals("tighten")){
    int clearance = Integer.parseInt(query_parts[1]);
    int size = Integer.parseInt(query_parts[2]);
    for(Tool t : tools){
      if(t instanceof Wrench){
        Wrench w = (Wrench)t;
        if(w.tighten(clearance, size)){
          return t;
        }
      }
    }
    <mark>return ??;</mark>
  }else if(query_parts[0].equals("cut")){
    int length = Integer.parseInt(query_parts[1]);
    for(Tool t : tools){
      if(t instanceof Saw){
        Saw s = (Saw)t;
        if(s.cut(length; query_parts[2]))){
          return s;
        }
      }
    }
    <mark>return ??;</mark>
  }else{
    <mark>return ??;</mark>
  }
}</code></pre>
</section>


<section>
  <pre class="stretch" style="font-size: .38em"><code class="java">public static Tool findTool(Tool[] tools, String query){
  String[] query_parts = query.split(" ");
  if(query_parts[0].equals("tighten")){
    int clearance = Integer.parseInt(query_parts[1]);
    int size = Integer.parseInt(query_parts[2]);
    for(Tool t : tools){
      if(t instanceof Wrench){
        Wrench w = (Wrench)t;
        if(w.tighten(clearance, size)){
          return t;
        }
      }
    }
    <mark>return null;</mark>
  }else if(query_parts[0].equals("cut")){
    int length = Integer.parseInt(query_parts[1]);
    for(Tool t : tools){
      if(t instanceof Saw){
        Saw s = (Saw)t;
        if(s.cut(length; query_parts[2]))){
          return s;
        }
      }
    }
    <mark>return null;</mark>
  }else{
    <mark>return null;</mark>
  }
}</code></pre>
</section>

<section>
  <pre class="stretch" style="font-size: .38em"><code class="java">public static Tool findTool(Tool[] tools, String query){
  String[] query_parts = query.split(" ");
  if(query_parts[0].equals("tighten")){
    int clearance = Integer.parseInt(query_parts[1]);
    int size = Integer.parseInt(query_parts[2]);
    for(Tool t : tools){
      if(t instanceof Wrench){
        Wrench w = (Wrench)t;
        if(w.tighten(clearance, size)){
          return t;
        }
      }
    }
    return null;
  }else if(query_parts[0].equals("cut")){
    int length = Integer.parseInt(query_parts[1]);
    for(Tool t : tools){
      if(t instanceof Saw){
        Saw s = (Saw)t;
        if(s.cut(length; query_parts[2]))){
          return s;
        }
      }
    }
    return null;
  }else{
    return null;
  }
}</code></pre>
</section>

<section>
  <pre class="stretch" style="font-size: .38em"><code class="java">public static void main(String[] args){
  if(args.length != 1){
    System.out.println("Invalid Input");
    return;
  }

}</code></pre>
</section>


<section>
  <pre class="stretch" style="font-size: .38em"><code class="java">public static void main(String[] args){
  if(args.length != 1){
    System.out.println("Invalid Input");
    return;
  }

  Tool[] tools = readInput(args[0]);

}</code></pre>
</section>

<section>
  <pre class="stretch" style="font-size: .38em"><code class="java">public static void main(String[] args){
  if(args.length != 1){
    System.out.println("Invalid Input");
    return;
  }

  Tool[] tools = readInput(args[0]);

  if(tools.length == 0){
    return;
  }

}</code></pre>
</section>

<section>
  <pre class="stretch" style="font-size: .38em"><code class="java">public static void main(String[] args){
  if(args.length != 1){
    System.out.println("Invalid Input");
    return;
  }

  Tool[] tools = readInput(args[0]);

  if(tools.length == 0){
    return;
  }

  try(
    Scanner scanner = new Scanner(System.in)
  ){



  }catch(Exception e){
    System.out.println("Invalid Tool");
    return;
  }
}</code></pre>
</section>

<section>
  <pre class="stretch" style="font-size: .38em"><code class="java">public static void main(String[] args){
  if(args.length != 1){
    System.out.println("Invalid Input");
    return;
  }

  Tool[] tools = readInput(args[0]);

  if(tools.length == 0){
    return;
  }

  try(
    Scanner scanner = new Scanner(System.in)
  ){

    String query = scanner.nextLine();
    Tool t = findTool(tools, query);


  }catch(Exception e){
    System.out.println("Invalid Tool");
    return;
  }
}</code></pre>
</section>

<section>
  <pre class="stretch" style="font-size: .38em"><code class="java">public static void main(String[] args){
  if(args.length != 1){
    System.out.println("Invalid Input");
    return;
  }

  Tool[] tools = readInput(args[0]);

  if(tools.length == 0){
    return;
  }

  try(
    Scanner scanner = new Scanner(System.in)
  ){

    String query = scanner.nextLine();
    Tool t = findTool(tools, query);
    if(t != null){
      System.out.println(t.describe());
    }else{
      System.out.println("Invalid Tool");
    }

  }catch(Exception e){
    System.out.println("Invalid Tool");
    return;
  }
}</code></pre>
</section>