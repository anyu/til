# Maven

## What is Apache Maven?
An open-source build automation & management tool for Java-based projects.

- based on Project Object Model (POM)
- more powerful than Ant, Make

## Benefits
- facilitates building project; takes care of:
  - generates any auto-generated source code & docs from code
  - compiles source code
  - packages compiled code into JAR file
  - uploads packaged code to local or central repo
- simplifies downloading JAR files and dependencies (download from centralized source instead of having to retrieve from multiple sources)
- provides uniform build process
- provides easy access to project info
- helps manage building/documenting/releasing/distributing Java projects

## POM
- an XML file with info on project and config details
- when a task is executed, Maven searches for the POM file

---

# Maven Build Lifecycle + commands

Maven's three built-in lifecycles (each consists of sequence of phases):
- **default**: main lifecycle (has 23 phases)
- **clean**: clean lifecycle (has 3 phases)
- **site**: generate docs (has 4 phases)

[List of phases in each lifecycle](https://maven.apache.org/guides/introduction/introduction-to-the-lifecycle.html#lifecycle-reference)

```shell
# executes all preceding phases up until specified phase
mvn <PHASE>
```

### Common phases to run selectively

```shell
# delete old build files
mvn clean

# run checks on results of integration test
mvn verify

# run all tests
mvn test

# package project into JAR
mvn package

# place project into local Maven repo
mvn install

# place project into remote Maven repo (essentially full default lifecycle)
mvn deploy
```

### Common flags
```
# specify path to POM if not in current dir
mvn -f <PATH TO POM>

# compile but skip tests
mvn clean install -DskipTests
```

#### Set properties in the POM file via `-D`
```
mvn -DpropertyName1=propertyVal1 -DpropertyName2=propertyVal2 package
```

pom.xml (before)
```
<properties>
    <theme>someDefaultTheme</theme>
</properties>
```

Run command with `-D`
```
mvn -Dtheme=halloween package
```

pom.xml (after)
```
<properties>
    <theme>halloween</theme>
</properties>
```
