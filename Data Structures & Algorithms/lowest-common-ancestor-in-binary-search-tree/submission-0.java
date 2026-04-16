/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        List<TreeNode> path_p = pathToNode(root, p);
        List<TreeNode> path_q = pathToNode(root, q);
        TreeNode ancestor = root;
        for (int i = 0; i < Math.min(path_p.size(), path_q.size()); i++) {
            if (path_p.get(i).val != path_q.get(i).val) {
                return ancestor;
            }
            ancestor = path_p.get(i);
        }
        return ancestor;
    }

    private List<TreeNode> pathToNode(TreeNode root, TreeNode n) {
        TreeNode curr = root;
        List<TreeNode> path = new ArrayList<>();
        path.add(curr);
        while (curr.val != n.val){
            if (n.val > curr.val){
                curr = curr.right;
            }
            else {
                curr = curr.left;
            }
            path.add(curr);
        }

        return path;
    }
}
