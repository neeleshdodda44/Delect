function update_threshold() {
  document.getElementById('thresholdb').value = document.getElementById('threshold').value
}

function RegisterController($scope,$http){
  $scope.details=[];

  $scope.foodList=[];
  
  $scope.adddetails=function(){
    $scope.details.push({'firstname':$scope.firstname, 'id':$scope.details.length})
    $scope.foodList.push($scope.firstname);
    $scope.firstname="";
    console.log($scope.foodList)

    var foods = "";
    if ($scope.foodList.length >= 1) {
      foods = $scope.foodList[0]
      if ($scope.foodList.length >= 2) {
        var index = 1;
        while (index < $scope.foodList.length) {
          foods = foods + "," + $scope.foodList[index];
          index ++;
        }
      }
    }
    document.getElementById('submitb').value = foods;
    $scope.frm.$setPristine();
  }
  
  $scope.deletedetail=function(index){
     $scope.details.splice(index,1);  
    $("#del").fadeOut(2000);
  };

   $scope.submit=function(){
      var threshold = $scope.threshold;
     
 // $scope.details.push({'firstname':$scope.firstname, 'id':$scope.details.length})
 //    $scope.firstname="";
    
 //    $scope.frm.$setPristine();
  }
  
  $scope.tickcross={};
  
  for (var i = 0, length = $scope.details.length; i < length; i++) {
      $scope.tickcross[$scope.details[i].id] = false;
    }
  
  //$scope.tickcross=false;
  
  $scope.modify=function(data){     
      //$scope.tickcross=true;
      $scope.tickcross[data.id]=true;
      console.log(data)
  }
  
  $scope.update=function(data){
     // $scope.tickcross=false;    
      $scope.tickcross[data.id]=false;          
  }
  
}